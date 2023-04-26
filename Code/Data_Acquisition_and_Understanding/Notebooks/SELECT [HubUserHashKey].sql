SELECT  [HubUserHashKey]
      ,[LoadDate]
      ,[RecordSource]
      ,[SatUserHashDiff]
      ,[ActivationState]
      ,[AuditIsVisible]
      ,[CAT]
      ,[cdcstatus]
      ,[cdctimestamp]
      ,[Code]
      ,[CompleteName]
      ,[CountryCode]
      ,[CountryNorm]
      ,[CountryVersion]
      ,[CreateAppName]
      ,[CreateAuthor]
      ,[CreateCompanyCode]
      ,[CreateDate]
      ,[CreateSubstitute]
      ,[CreateSubstituteRole]
      ,[CreateTransactionId]
      ,[CultureCode]
      ,[DefaultApplicationUserProfileName]
      ,[DefaultMarketplaceConfiguration]
      ,[DisplayName]
      ,[EmployeeNumber]
      ,[Gender]
      ,[IndependentWork]
      ,[InHighContrastMode]
      ,[IsBlocked]
      ,[isCompanyDefaultSettings]
      ,[IsDeleted]
      ,[IsDraft]
      ,[IsFirstLogin]
      ,[JobTitle]
      ,[LanguageCode]
      ,[OldId]
      ,[PersistOrder]
      ,[RegistrationDate]
      ,[SecurityAnswer]
      ,[SecurityQuestion]
      ,[SelectedSecurityQuestion]
      ,[TimeZoneRefDataCode]
      ,[Title]
      ,[Type]
      ,[UserCulture]
      ,[UserImage]
      ,[UserImageDataCrop]
      ,[UserPhotoFileId]
      ,[VersionAppName]
      ,[VersionAuthor]
      ,[VersionCompanyCode]
      ,[VersionDate]
      ,[VersionNumber]
      ,[VersionSubstitute]
      ,[VersionSubstituteRole]
      ,[VersionTransactionId]
      ,[WasCreatedByOthers]
      ,[Deleted]
      ,[Surname]
      ,[EducationalLevel]
      ,[BirthDate]
  FROM [CCE_Sandbox].[datavault].[Sat_User]
  WHERE [Code] like '%114229%'