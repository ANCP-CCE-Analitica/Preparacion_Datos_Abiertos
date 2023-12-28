import pandas as pd
from fuzzywuzzy import fuzz


def entity_master_to_dict(entity_master):
    entity_dict = {}
    
    for id in entity_master['ID'].unique():
        entity_dict[id] = entity_master[entity_master['ID'] == id]
    return  entity_dict

def update_entity_master_dict(new_registers, entity_master, threshold=89):
    entity_dict = entity_master_to_dict(entity_master)
    new_entities = new_registers.sort_values('ENTIDAD')
    id_counter = entity_master['ID'].max() if entity_master.shape[0] > 0 else 0
    grupos_por_entidad = new_registers.groupby(['ENTIDAD', 'NIT', 'ID_SECOP'])

    for key_group, group in grupos_por_entidad:
        flag = False
        for key in entity_dict:
            if not entity_dict[key].empty:
                if (key_group[0] in entity_dict[key]['ENTIDAD'].values) or \
                    (key_group[2] in entity_dict[key]['ID_SECOP'].values):
                    entity_dict[key] = pd.concat([entity_dict[key], new_registers.loc[
                        (new_registers['ENTIDAD'] == key_group[0]) &
                        (new_registers['NIT'] == key_group[1]) &
                        (new_registers['ID_SECOP'] == key_group[2])]])
                    flag = True
                    break
                else:
                    for nit in entity_dict[key]['NIT'].unique():
                        if pd.notnull(nit) and pd.notnull(key_group[1]) and len(str(nit)) >= 7 and len(str(key_group[1])) >= 7:
                            if fuzz.partial_ratio(str(key_group[1]), str(nit)) >= threshold:
                                entity_dict[key] = pd.concat([entity_dict[key], new_registers.loc[
                                    (new_registers['ENTIDAD'] == key_group[0]) &
                                    (new_registers['NIT'] == key_group[1]) &
                                    (new_registers['ID_SECOP'] == key_group[2])]])
                                flag = True
                                break
                    
        if not flag:
            entity_dict[id_counter] = new_registers.loc[(new_registers['ENTIDAD'] == key_group[0]) &
                                                        (new_registers['NIT'] == key_group[1]) &
                                                        (new_registers['ID_SECOP'] == key_group[2])]
            id_counter += 1
    return entity_dict

def update_entity_master(new_registers, entity_master, threshold=95, path='../../../muestras de datos/procesados/silver/maestro_entidades.csv'):
    entity_master_dict = update_entity_master_dict(new_registers, entity_master, threshold)
    for key in entity_master_dict:
        entity_master_dict[key]['ID'] = key
    entity_master = pd.concat(entity_master_dict.values())
    entity_master = entity_master.sort_values(by='ID')
    entity_master_updated = entity_master[['ID', 'ID_SECOP', 'ENTIDAD', 'NIT', 'ORDEN', 'DEPARTAMENTO', 'MUNICIPIO']].drop_duplicates(subset=['NIT', 'ENTIDAD', 'ID_SECOP'], keep='first')
    entity_master_updated.to_csv(path, sep=';', index=False)
    return entity_master