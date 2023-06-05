SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

/*
truncate table [SECOPII].[T_HistoricoProcedimientos_Despliegue]
go
Insert into [SECOPII].[T_HistoricoProcedimientos_Despliegue]
Select * from [10.240.5.38].[DM-CCE-TENDERING].[CCE].[HistoricoProcedimientos_Despliegue]
GO
*/

CREATE VIEW  [SECOPII].[V_HistoricoProcedimientos] 
as 
Select 

HPD.[CompanyName], 
HPD.[BuyerVat], 
HPD.[PCICode], 
HPD.[ProcedureRequestID], 
HPD.[Reference], 
HPD.[PPI], 
HPD.[BuyerDossierID], 
HPD.[ProcedureRequestName], 
HPD.[ProcedureRequestDescription2], 
HPD.[ProfileDocUniqueName], 
HPD.[PhaseName], 
HPD.[RequestOnlinePublishingDate], 
HPD.[Fecha Publicación], 
HPD.[Fecha Publicacion fase planeacion precalficacion], 
HPD.[Fecha Publicacion fase seleccion precalficacion], 
HPD.[Fecha de Menifestacion de Interes], 
HPD.[Fecha de publicacion de la fase borrador], 
HPD.[Fecha de Publicacion de la fase Seleccion], 
Isnull ([DBA].Valor_Corregido, Isnull ([DBP].Valor_Corregido, HPD.[BasePrice])) as [BasePrice],
HPD.[SubmissionUser], 
HPD.[Market], 
HPD.[RequestType], 
HPD.[ProcedureRequestType], 
HPD.[OpenByCategory], 
HPD.[LegalFrameworkName], 
HPD.[Duration], 
HPD.[DurationType], 
HPD.[DueDateForReceivingReplies], 
HPD.[OpeningRepliesDate], 
HPD.[EffectiveOpeningDate], 
HPD.[BusinessOperationState], 
HPD.[BusinessOperationName], 
HPD.[BusinessOperationCountry], 
HPD.[AllowAuction], 
HPD.[SuppliersInvited], 
HPD.[DirectSuppliersInvited], 
HPD.[ProcedureVisualizationCount], 
HPD.[SuppliersExpressedInterestCount], 
HPD.[RepliesCount], 
HPD.[ExternalRepliesCount], 
HPD.[CounterProposalRepliesCount], 
HPD.[DistinctSupplierWithReplies], 
HPD.[NumLotes], 
HPD.[ProcedureRequestDescription], 
HPD.[ProcedureRequestState], 
HPD.[ProcedureRequestStateId], 
HPD.[Awarded], 
HPD.[Award ID], 
HPD.[AwardDate], 
HPD.[AwardTotalPrice], 
HPD.[AwarderDisplayName], 
HPD.[SupplierName], 
HPD.[SupplierVat], 
HPD.[SupplierPhoneNumber], 
HPD.[SupplierEmailAddress], 
HPD.[DimMainCategoryCode], 
HPD.[DimMainCategoryTypeCode], 
HPD.[ProcedureRequestOpeningState], 
HPD.[TypeOfContract], 
HPD.[SubTypeOfContract], 
HPD.[AddicionalCategoryCodes], 
HPD.[Tipo], 
HPD.[CodigoProveedor], 
HPD.[ContractNoticeUniqueIdentifier], 
HPD.[Departamento Entidad], 
HPD.[Ciudad Entidad], 
HPD.[Departamento Proveedor], 
HPD.[Ciudad Proveedor], 
HPD.[ProcedureCurrencyCode] as [Codigo Moneda], 
HPD.[NumberOfAmendments] as [NumeroAdendas], 
HPD.[AdtEditedAt], 
HPD.[Orden] as [OrdenEntidad], 
HPD.[Justificación Modalidad de Contratación], 
HPD.[Entidad Centralizada],
'https://community.secop.gov.co/Public/Tendering/OpportunityDetail/Index?noticeUID=' + convert (varchar(50), HPD.ContractNoticeUniqueIdentifier) + '&isFromPublicArea=True&isModal=true&asPopupView=true' as URLProceso


FROM [SECOPII].[HistoricoProcedimientos_Despliegue] HPD  (NOLOCK) -- [10.240.5.38].[DM-CCE-TENDERING].[CCE].[HistoricoProcedimientos_Despliegue] HPD
left JOIN (select * from [SECOPII].DepuracionBaseSII where Tipo = 'Procesos') DBP on HPD.BuyerDossierID = DBP.ID_Proceso
  and HPD.Reference = DBP.Referencia_Proceso and HPD.BasePrice = DBP.Valor_original
left JOIN (select * from [SECOPII].DepuracionBaseSII where  Tipo = 'Adjudicación') DBA on HPD.BuyerDossierID = DBA.ID_Proceso
  and HPD.Reference = DBA.Referencia_Proceso and HPD.AwardTotalPrice= DBA.Valor_original
where HPD.ProcedureRequestType <> 'Subasta de prueba' and HPD.ProcedureRequestState <> 'Cancelado' 




GO
