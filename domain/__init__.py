from json import dumps


class DestinyTables:

    def __init__(self,
                 DestinyNodeStepSummaryDefinition: str,
                 DestinyArtDyeChannelDefinition: str,
                 DestinyArtDyeReferenceDefinition: str,
                 DestinyPlaceDefinition: str,
                 DestinyActivityDefinition: str,
                 DestinyActivityTypeDefinition: str,
                 DestinyClassDefinition: str,
                 DestinyGenderDefinition: str,
                 DestinyInventoryBucketDefinition: str,
                 DestinyRaceDefinition: str,
                 DestinyTalentGridDefinition: str,
                 DestinyUnlockDefinition: str,
                 DestinyStatGroupDefinition: str,
                 DestinyProgressionMappingDefinition: str,
                 DestinyFactionDefinition: str,
                 DestinyVendorGroupDefinition: str,
                 DestinyRewardSourceDefinition: str,
                 DestinyUnlockValueDefinition: str,
                 DestinyRewardMappingDefinition: str,
                 DestinyRewardSheetDefinition: str,
                 DestinyItemCategoryDefinition: str,
                 DestinyDamageTypeDefinition: str,
                 DestinyActivityModeDefinition: str,
                 DestinyMedalTierDefinition: str,
                 DestinyAchievementDefinition: str,
                 DestinyActivityGraphDefinition: str,
                 DestinyActivityInteractableDefinition: str,
                 DestinyBondDefinition: str,
                 DestinyCharacterCustomizationCategoryDefinition: str,
                 DestinyCharacterCustomizationOptionDefinition: str,
                 DestinyCollectibleDefinition: str,
                 DestinyDestinationDefinition: str,
                 DestinyEntitlementOfferDefinition: str,
                 DestinyEquipmentSlotDefinition: str,
                 DestinyEventCardDefinition: str,
                 DestinyFireteamFinderActivityGraphDefinition: str,
                 DestinyFireteamFinderActivitySetDefinition: str,
                 DestinyFireteamFinderLabelDefinition: str,
                 DestinyFireteamFinderLabelGroupDefinition: str,
                 DestinyFireteamFinderOptionDefinition: str,
                 DestinyFireteamFinderOptionGroupDefinition: str,
                 DestinyStatDefinition: str,
                 DestinyInventoryItemDefinition: str,
                 DestinyInventoryItemLiteDefinition: str,
                 DestinyItemTierTypeDefinition: str,
                 DestinyLoadoutColorDefinition: str,
                 DestinyLoadoutIconDefinition: str,
                 DestinyLoadoutNameDefinition: str,
                 DestinyLocationDefinition: str,
                 DestinyLoreDefinition: str,
                 DestinyMaterialRequirementSetDefinition: str,
                 DestinyMetricDefinition: str,
                 DestinyObjectiveDefinition: str,
                 DestinySandboxPerkDefinition: str,
                 DestinyPlatformBucketMappingDefinition: str,
                 DestinyPlugSetDefinition: str,
                 DestinyPowerCapDefinition: str,
                 DestinyPresentationNodeDefinition: str,
                 DestinyProgressionDefinition: str,
                 DestinyProgressionLevelRequirementDefinition: str,
                 DestinyRecordDefinition: str,
                 DestinyRewardAdjusterPointerDefinition: str,
                 DestinyRewardAdjusterProgressionMapDefinition: str,
                 DestinyRewardItemListDefinition: str,
                 DestinySackRewardItemListDefinition: str,
                 DestinySandboxPatternDefinition: str,
                 DestinySeasonDefinition: str,
                 DestinySeasonPassDefinition: str,
                 DestinySocialCommendationDefinition: str,
                 DestinySocketCategoryDefinition: str,
                 DestinySocketTypeDefinition: str,
                 DestinyTraitDefinition: str,
                 DestinyUnlockCountMappingDefinition: str,
                 DestinyUnlockEventDefinition: str,
                 DestinyUnlockExpressionMappingDefinition: str,
                 DestinyVendorDefinition: str,
                 DestinyMilestoneDefinition: str,
                 DestinyActivityModifierDefinition: str,
                 DestinyReportReasonCategoryDefinition: str,
                 DestinyArtifactDefinition: str,
                 DestinyBreakerTypeDefinition: str,
                 DestinyChecklistDefinition: str,
                 DestinyEnergyTypeDefinition: str,
                 DestinySocialCommendationNodeDefinition: str,
                 DestinyGuardianRankDefinition: str,
                 DestinyGuardianRankConstantsDefinition: str,
                 DestinyLoadoutConstantsDefinition: str,
                 DestinyFireteamFinderConstantsDefinition: str
                 ):
        self.DestinyNodeStepSummaryDefinition = DestinyNodeStepSummaryDefinition
        self.DestinyArtDyeChannelDefinition = DestinyArtDyeChannelDefinition
        self.DestinyArtDyeReferenceDefinition = DestinyArtDyeReferenceDefinition
        self.DestinyPlaceDefinition = DestinyPlaceDefinition
        self.DestinyActivityDefinition = DestinyActivityDefinition
        self.DestinyActivityTypeDefinition = DestinyActivityTypeDefinition
        self.DestinyClassDefinition = DestinyClassDefinition
        self.DestinyGenderDefinition = DestinyGenderDefinition
        self.DestinyInventoryBucketDefinition = DestinyInventoryBucketDefinition
        self.DestinyRaceDefinition = DestinyRaceDefinition
        self.DestinyTalentGridDefinition = DestinyTalentGridDefinition
        self.DestinyUnlockDefinition = DestinyUnlockDefinition
        self.DestinyStatGroupDefinition = DestinyStatGroupDefinition
        self.DestinyProgressionMappingDefinition = DestinyProgressionMappingDefinition
        self.DestinyFactionDefinition = DestinyFactionDefinition
        self.DestinyVendorGroupDefinition = DestinyVendorGroupDefinition
        self.DestinyRewardSourceDefinition = DestinyRewardSourceDefinition
        self.DestinyUnlockValueDefinition = DestinyUnlockValueDefinition
        self.DestinyRewardMappingDefinition = DestinyRewardMappingDefinition
        self.DestinyRewardSheetDefinition = DestinyRewardSheetDefinition
        self.DestinyItemCategoryDefinition = DestinyItemCategoryDefinition
        self.DestinyDamageTypeDefinition = DestinyDamageTypeDefinition
        self.DestinyActivityModeDefinition = DestinyActivityModeDefinition
        self.DestinyMedalTierDefinition = DestinyMedalTierDefinition
        self.DestinyAchievementDefinition = DestinyAchievementDefinition
        self.DestinyActivityGraphDefinition = DestinyActivityGraphDefinition
        self.DestinyActivityInteractableDefinition = DestinyActivityInteractableDefinition
        self.DestinyBondDefinition = DestinyBondDefinition
        self.DestinyCharacterCustomizationCategoryDefinition = DestinyCharacterCustomizationCategoryDefinition
        self.DestinyCharacterCustomizationOptionDefinition = DestinyCharacterCustomizationOptionDefinition
        self.DestinyCollectibleDefinition = DestinyCollectibleDefinition
        self.DestinyDestinationDefinition = DestinyDestinationDefinition
        self.DestinyEntitlementOfferDefinition = DestinyEntitlementOfferDefinition
        self.DestinyEquipmentSlotDefinition = DestinyEquipmentSlotDefinition
        self.DestinyEventCardDefinition = DestinyEventCardDefinition
        self.DestinyFireteamFinderActivityGraphDefinition = DestinyFireteamFinderActivityGraphDefinition
        self.DestinyFireteamFinderActivitySetDefinition = DestinyFireteamFinderActivitySetDefinition
        self.DestinyFireteamFinderLabelDefinition = DestinyFireteamFinderLabelDefinition
        self.DestinyFireteamFinderLabelGroupDefinition = DestinyFireteamFinderLabelGroupDefinition
        self.DestinyFireteamFinderOptionDefinition = DestinyFireteamFinderOptionDefinition
        self.DestinyFireteamFinderOptionGroupDefinition = DestinyFireteamFinderOptionGroupDefinition
        self.DestinyStatDefinition = DestinyStatDefinition
        self.DestinyInventoryItemDefinition = DestinyInventoryItemDefinition
        self.DestinyInventoryItemLiteDefinition = DestinyInventoryItemLiteDefinition
        self.DestinyItemTierTypeDefinition = DestinyItemTierTypeDefinition
        self.DestinyLoadoutColorDefinition = DestinyLoadoutColorDefinition
        self.DestinyLoadoutIconDefinition = DestinyLoadoutIconDefinition
        self.DestinyLoadoutNameDefinition = DestinyLoadoutNameDefinition
        self.DestinyLocationDefinition = DestinyLocationDefinition
        self.DestinyLoreDefinition = DestinyLoreDefinition
        self.DestinyMaterialRequirementSetDefinition = DestinyMaterialRequirementSetDefinition
        self.DestinyMetricDefinition = DestinyMetricDefinition
        self.DestinyObjectiveDefinition = DestinyObjectiveDefinition
        self.DestinySandboxPerkDefinition = DestinySandboxPerkDefinition
        self.DestinyPlatformBucketMappingDefinition = DestinyPlatformBucketMappingDefinition
        self.DestinyPlugSetDefinition = DestinyPlugSetDefinition
        self.DestinyPowerCapDefinition = DestinyPowerCapDefinition
        self.DestinyPresentationNodeDefinition = DestinyPresentationNodeDefinition
        self.DestinyProgressionDefinition = DestinyProgressionDefinition
        self.DestinyProgressionLevelRequirementDefinition = DestinyProgressionLevelRequirementDefinition
        self.DestinyRecordDefinition = DestinyRecordDefinition
        self.DestinyRewardAdjusterPointerDefinition = DestinyRewardAdjusterPointerDefinition
        self.DestinyRewardAdjusterProgressionMapDefinition = DestinyRewardAdjusterProgressionMapDefinition
        self.DestinyRewardItemListDefinition = DestinyRewardItemListDefinition
        self.DestinySackRewardItemListDefinition = DestinySackRewardItemListDefinition
        self.DestinySandboxPatternDefinition = DestinySandboxPatternDefinition
        self.DestinySeasonDefinition = DestinySeasonDefinition
        self.DestinySeasonPassDefinition = DestinySeasonPassDefinition
        self.DestinySocialCommendationDefinition = DestinySocialCommendationDefinition
        self.DestinySocketCategoryDefinition = DestinySocketCategoryDefinition
        self.DestinySocketTypeDefinition = DestinySocketTypeDefinition
        self.DestinyTraitDefinition = DestinyTraitDefinition
        self.DestinyUnlockCountMappingDefinition = DestinyUnlockCountMappingDefinition
        self.DestinyUnlockEventDefinition = DestinyUnlockEventDefinition
        self.DestinyUnlockExpressionMappingDefinition = DestinyUnlockExpressionMappingDefinition
        self.DestinyVendorDefinition = DestinyVendorDefinition
        self.DestinyMilestoneDefinition = DestinyMilestoneDefinition
        self.DestinyActivityModifierDefinition = DestinyActivityModifierDefinition
        self.DestinyReportReasonCategoryDefinition = DestinyReportReasonCategoryDefinition
        self.DestinyArtifactDefinition = DestinyArtifactDefinition
        self.DestinyBreakerTypeDefinition = DestinyBreakerTypeDefinition
        self.DestinyChecklistDefinition = DestinyChecklistDefinition
        self.DestinyEnergyTypeDefinition = DestinyEnergyTypeDefinition
        self.DestinySocialCommendationNodeDefinition = DestinySocialCommendationNodeDefinition
        self.DestinyGuardianRankDefinition = DestinyGuardianRankDefinition
        self.DestinyGuardianRankConstantsDefinition = DestinyGuardianRankConstantsDefinition
        self.DestinyLoadoutConstantsDefinition = DestinyLoadoutConstantsDefinition
        self.DestinyFireteamFinderConstantsDefinition = DestinyFireteamFinderConstantsDefinition

    @classmethod
    def From(cls, value: dict):
        return cls(
            value["DestinyNodeStepSummaryDefinition"],
            value["DestinyArtDyeChannelDefinition"],
            value["DestinyArtDyeReferenceDefinition"],
            value["DestinyPlaceDefinition"],
            value["DestinyActivityDefinition"],
            value["DestinyActivityTypeDefinition"],
            value["DestinyClassDefinition"],
            value["DestinyGenderDefinition"],
            value["DestinyInventoryBucketDefinition"],
            value["DestinyRaceDefinition"],
            value["DestinyTalentGridDefinition"],
            value["DestinyUnlockDefinition"],
            value["DestinyStatGroupDefinition"],
            value["DestinyProgressionMappingDefinition"],
            value["DestinyFactionDefinition"],
            value["DestinyVendorGroupDefinition"],
            value["DestinyRewardSourceDefinition"],
            value["DestinyUnlockValueDefinition"],
            value["DestinyRewardMappingDefinition"],
            value["DestinyRewardSheetDefinition"],
            value["DestinyItemCategoryDefinition"],
            value["DestinyDamageTypeDefinition"],
            value["DestinyActivityModeDefinition"],
            value["DestinyMedalTierDefinition"],
            value["DestinyAchievementDefinition"],
            value["DestinyActivityGraphDefinition"],
            value["DestinyActivityInteractableDefinition"],
            value["DestinyBondDefinition"],
            value["DestinyCharacterCustomizationCategoryDefinition"],
            value["DestinyCharacterCustomizationOptionDefinition"],
            value["DestinyCollectibleDefinition"],
            value["DestinyDestinationDefinition"],
            value["DestinyEntitlementOfferDefinition"],
            value["DestinyEquipmentSlotDefinition"],
            value["DestinyEventCardDefinition"],
            value["DestinyFireteamFinderActivityGraphDefinition"],
            value["DestinyFireteamFinderActivitySetDefinition"],
            value["DestinyFireteamFinderLabelDefinition"],
            value["DestinyFireteamFinderLabelGroupDefinition"],
            value["DestinyFireteamFinderOptionDefinition"],
            value["DestinyFireteamFinderOptionGroupDefinition"],
            value["DestinyStatDefinition"],
            value["DestinyInventoryItemDefinition"],
            value["DestinyInventoryItemLiteDefinition"],
            value["DestinyItemTierTypeDefinition"],
            value["DestinyLoadoutColorDefinition"],
            value["DestinyLoadoutIconDefinition"],
            value["DestinyLoadoutNameDefinition"],
            value["DestinyLocationDefinition"],
            value["DestinyLoreDefinition"],
            value["DestinyMaterialRequirementSetDefinition"],
            value["DestinyMetricDefinition"],
            value["DestinyObjectiveDefinition"],
            value["DestinySandboxPerkDefinition"],
            value["DestinyPlatformBucketMappingDefinition"],
            value["DestinyPlugSetDefinition"],
            value["DestinyPowerCapDefinition"],
            value["DestinyPresentationNodeDefinition"],
            value["DestinyProgressionDefinition"],
            value["DestinyProgressionLevelRequirementDefinition"],
            value["DestinyRecordDefinition"],
            value["DestinyRewardAdjusterPointerDefinition"],
            value["DestinyRewardAdjusterProgressionMapDefinition"],
            value["DestinyRewardItemListDefinition"],
            value["DestinySackRewardItemListDefinition"],
            value["DestinySandboxPatternDefinition"],
            value["DestinySeasonDefinition"],
            value["DestinySeasonPassDefinition"],
            value["DestinySocialCommendationDefinition"],
            value["DestinySocketCategoryDefinition"],
            value["DestinySocketTypeDefinition"],
            value["DestinyTraitDefinition"],
            value["DestinyUnlockCountMappingDefinition"],
            value["DestinyUnlockEventDefinition"],
            value["DestinyUnlockExpressionMappingDefinition"],
            value["DestinyVendorDefinition"],
            value["DestinyMilestoneDefinition"],
            value["DestinyActivityModifierDefinition"],
            value["DestinyReportReasonCategoryDefinition"],
            value["DestinyArtifactDefinition"],
            value["DestinyBreakerTypeDefinition"],
            value["DestinyChecklistDefinition"],
            value["DestinyEnergyTypeDefinition"],
            value["DestinySocialCommendationNodeDefinition"],
            value["DestinyGuardianRankDefinition"],
            value["DestinyGuardianRankConstantsDefinition"],
            value["DestinyLoadoutConstantsDefinition"],
            value["DestinyFireteamFinderConstantsDefinition"]
        )

    def __dict__(self):
        return {
            "DestinyNodeStepSummaryDefinition": self.DestinyNodeStepSummaryDefinition,
            "DestinyArtDyeChannelDefinition": self.DestinyArtDyeChannelDefinition,
            "DestinyArtDyeReferenceDefinition": self.DestinyArtDyeReferenceDefinition,
            "DestinyPlaceDefinition": self.DestinyPlaceDefinition,
            "DestinyActivityDefinition": self.DestinyActivityDefinition,
            "DestinyActivityTypeDefinition": self.DestinyActivityTypeDefinition,
            "DestinyClassDefinition": self.DestinyClassDefinition,
            "DestinyGenderDefinition": self.DestinyGenderDefinition,
            "DestinyInventoryBucketDefinition": self.DestinyInventoryBucketDefinition,
            "DestinyRaceDefinition": self.DestinyRaceDefinition,
            "DestinyTalentGridDefinition": self.DestinyTalentGridDefinition,
            "DestinyUnlockDefinition": self.DestinyUnlockDefinition,
            "DestinyStatGroupDefinition": self.DestinyStatGroupDefinition,
            "DestinyProgressionMappingDefinition": self.DestinyProgressionMappingDefinition,
            "DestinyFactionDefinition": self.DestinyFactionDefinition,
            "DestinyVendorGroupDefinition": self.DestinyVendorGroupDefinition,
            "DestinyRewardSourceDefinition": self.DestinyRewardSourceDefinition,
            "DestinyUnlockValueDefinition": self.DestinyUnlockValueDefinition,
            "DestinyRewardMappingDefinition": self.DestinyRewardMappingDefinition,
            "DestinyRewardSheetDefinition": self.DestinyRewardSheetDefinition,
            "DestinyItemCategoryDefinition": self.DestinyItemCategoryDefinition,
            "DestinyDamageTypeDefinition": self.DestinyDamageTypeDefinition,
            "DestinyActivityModeDefinition": self.DestinyActivityModeDefinition,
            "DestinyMedalTierDefinition": self.DestinyMedalTierDefinition,
            "DestinyAchievementDefinition": self.DestinyAchievementDefinition,
            "DestinyActivityGraphDefinition": self.DestinyActivityGraphDefinition,
            "DestinyActivityInteractableDefinition": self.DestinyActivityInteractableDefinition,
            "DestinyBondDefinition": self.DestinyBondDefinition,
            "DestinyCharacterCustomizationCategoryDefinition": self.DestinyCharacterCustomizationCategoryDefinition,
            "DestinyCharacterCustomizationOptionDefinition": self.DestinyCharacterCustomizationOptionDefinition,
            "DestinyCollectibleDefinition": self.DestinyCollectibleDefinition,
            "DestinyDestinationDefinition": self.DestinyDestinationDefinition,
            "DestinyEntitlementOfferDefinition": self.DestinyEntitlementOfferDefinition,
            "DestinyEquipmentSlotDefinition": self.DestinyEquipmentSlotDefinition,
            "DestinyEventCardDefinition": self.DestinyEventCardDefinition,
            "DestinyFireteamFinderActivityGraphDefinition": self.DestinyFireteamFinderActivityGraphDefinition,
            "DestinyFireteamFinderActivitySetDefinition": self.DestinyFireteamFinderActivitySetDefinition,
            "DestinyFireteamFinderLabelDefinition": self.DestinyFireteamFinderLabelDefinition,
            "DestinyFireteamFinderLabelGroupDefinition": self.DestinyFireteamFinderLabelGroupDefinition,
            "DestinyFireteamFinderOptionDefinition": self.DestinyFireteamFinderOptionDefinition,
            "DestinyFireteamFinderOptionGroupDefinition": self.DestinyFireteamFinderOptionGroupDefinition,
            "DestinyStatDefinition": self.DestinyStatDefinition,
            "DestinyInventoryItemDefinition": self.DestinyInventoryItemDefinition,
            "DestinyInventoryItemLiteDefinition": self.DestinyInventoryItemLiteDefinition,
            "DestinyItemTierTypeDefinition": self.DestinyItemTierTypeDefinition,
            "DestinyLoadoutColorDefinition": self.DestinyLoadoutColorDefinition,
            "DestinyLoadoutIconDefinition": self.DestinyLoadoutIconDefinition,
            "DestinyLoadoutNameDefinition": self.DestinyLoadoutNameDefinition,
            "DestinyLocationDefinition": self.DestinyLocationDefinition,
            "DestinyLoreDefinition": self.DestinyLoreDefinition,
            "DestinyMaterialRequirementSetDefinition": self.DestinyMaterialRequirementSetDefinition,
            "DestinyMetricDefinition": self.DestinyMetricDefinition,
            "DestinyObjectiveDefinition": self.DestinyObjectiveDefinition,
            "DestinySandboxPerkDefinition": self.DestinySandboxPerkDefinition,
            "DestinyPlatformBucketMappingDefinition": self.DestinyPlatformBucketMappingDefinition,
            "DestinyPlugSetDefinition": self.DestinyPlugSetDefinition,
            "DestinyPowerCapDefinition": self.DestinyPowerCapDefinition,
            "DestinyPresentationNodeDefinition": self.DestinyPresentationNodeDefinition,
            "DestinyProgressionDefinition": self.DestinyProgressionDefinition,
            "DestinyProgressionLevelRequirementDefinition": self.DestinyProgressionLevelRequirementDefinition,
            "DestinyRecordDefinition": self.DestinyRecordDefinition,
            "DestinyRewardAdjusterPointerDefinition": self.DestinyRewardAdjusterPointerDefinition,
            "DestinyRewardAdjusterProgressionMapDefinition": self.DestinyRewardAdjusterProgressionMapDefinition,
            "DestinyRewardItemListDefinition": self.DestinyRewardItemListDefinition,
            "DestinySackRewardItemListDefinition": self.DestinySackRewardItemListDefinition,
            "DestinySandboxPatternDefinition": self.DestinySandboxPatternDefinition,
            "DestinySeasonDefinition": self.DestinySeasonDefinition,
            "DestinySeasonPassDefinition": self.DestinySeasonPassDefinition,
            "DestinySocialCommendationDefinition": self.DestinySocialCommendationDefinition,
            "DestinySocketCategoryDefinition": self.DestinySocketCategoryDefinition,
            "DestinySocketTypeDefinition": self.DestinySocketTypeDefinition,
            "DestinyTraitDefinition": self.DestinyTraitDefinition,
            "DestinyUnlockCountMappingDefinition": self.DestinyUnlockCountMappingDefinition,
            "DestinyUnlockEventDefinition": self.DestinyUnlockEventDefinition,
            "DestinyUnlockExpressionMappingDefinition": self.DestinyUnlockExpressionMappingDefinition,
            "DestinyVendorDefinition": self.DestinyVendorDefinition,
            "DestinyMilestoneDefinition": self.DestinyMilestoneDefinition,
            "DestinyActivityModifierDefinition": self.DestinyActivityModifierDefinition,
            "DestinyReportReasonCategoryDefinition": self.DestinyReportReasonCategoryDefinition,
            "DestinyArtifactDefinition": self.DestinyArtifactDefinition,
            "DestinyBreakerTypeDefinition": self.DestinyBreakerTypeDefinition,
            "DestinyChecklistDefinition": self.DestinyChecklistDefinition,
            "DestinyEnergyTypeDefinition": self.DestinyEnergyTypeDefinition,
            "DestinySocialCommendationNodeDefinition": self.DestinySocialCommendationNodeDefinition,
            "DestinyGuardianRankDefinition": self.DestinyGuardianRankDefinition,
            "DestinyGuardianRankConstantsDefinition": self.DestinyGuardianRankConstantsDefinition,
            "DestinyLoadoutConstantsDefinition": self.DestinyLoadoutConstantsDefinition,
            "DestinyFireteamFinderConstantsDefinition": self.DestinyFireteamFinderConstantsDefinition
        }

    def __str__(self):
        return dumps(self.__dict__())

    def __iter__(self):
        return iter(
            [self.DestinyNodeStepSummaryDefinition, self.DestinyArtDyeChannelDefinition, self.DestinyArtDyeReferenceDefinition, self.DestinyPlaceDefinition,
             self.DestinyActivityDefinition, self.DestinyActivityTypeDefinition, self.DestinyClassDefinition, self.DestinyGenderDefinition,
             self.DestinyInventoryBucketDefinition, self.DestinyRaceDefinition, self.DestinyTalentGridDefinition, self.DestinyUnlockDefinition,
             self.DestinyStatGroupDefinition, self.DestinyProgressionMappingDefinition, self.DestinyFactionDefinition, self.DestinyVendorGroupDefinition,
             self.DestinyRewardSourceDefinition, self.DestinyUnlockValueDefinition, self.DestinyRewardMappingDefinition, self.DestinyRewardSheetDefinition,
             self.DestinyItemCategoryDefinition, self.DestinyDamageTypeDefinition, self.DestinyActivityModeDefinition, self.DestinyMedalTierDefinition,
             self.DestinyAchievementDefinition, self.DestinyActivityGraphDefinition, self.DestinyActivityInteractableDefinition, self.DestinyBondDefinition,
             self.DestinyCharacterCustomizationCategoryDefinition, self.DestinyCharacterCustomizationOptionDefinition, self.DestinyCollectibleDefinition,
             self.DestinyDestinationDefinition, self.DestinyEntitlementOfferDefinition, self.DestinyEquipmentSlotDefinition, self.DestinyEventCardDefinition,
             self.DestinyFireteamFinderActivityGraphDefinition, self.DestinyFireteamFinderActivitySetDefinition, self.DestinyFireteamFinderLabelDefinition,
             self.DestinyFireteamFinderLabelGroupDefinition, self.DestinyFireteamFinderOptionDefinition, self.DestinyFireteamFinderOptionGroupDefinition,
             self.DestinyStatDefinition, self.DestinyInventoryItemDefinition, self.DestinyInventoryItemLiteDefinition, self.DestinyItemTierTypeDefinition,
             self.DestinyLoadoutColorDefinition, self.DestinyLoadoutIconDefinition, self.DestinyLoadoutNameDefinition, self.DestinyLocationDefinition,
             self.DestinyLoreDefinition, self.DestinyMaterialRequirementSetDefinition, self.DestinyMetricDefinition, self.DestinyObjectiveDefinition,
             self.DestinySandboxPerkDefinition, self.DestinyPlatformBucketMappingDefinition, self.DestinyPlugSetDefinition, self.DestinyPowerCapDefinition,
             self.DestinyPresentationNodeDefinition, self.DestinyProgressionDefinition, self.DestinyProgressionLevelRequirementDefinition,
             self.DestinyRecordDefinition, self.DestinyRewardAdjusterPointerDefinition, self.DestinyRewardAdjusterProgressionMapDefinition,
             self.DestinyRewardItemListDefinition, self.DestinySackRewardItemListDefinition, self.DestinySandboxPatternDefinition,
             self.DestinySeasonDefinition, self.DestinySeasonPassDefinition, self.DestinySocialCommendationDefinition, self.DestinySocketCategoryDefinition,
             self.DestinySocketTypeDefinition, self.DestinyTraitDefinition, self.DestinyUnlockCountMappingDefinition, self.DestinyUnlockEventDefinition,
             self.DestinyUnlockExpressionMappingDefinition, self.DestinyVendorDefinition, self.DestinyMilestoneDefinition,
             self.DestinyActivityModifierDefinition, self.DestinyReportReasonCategoryDefinition, self.DestinyArtifactDefinition,
             self.DestinyBreakerTypeDefinition, self.DestinyChecklistDefinition, self.DestinyEnergyTypeDefinition,
             self.DestinySocialCommendationNodeDefinition, self.DestinyGuardianRankDefinition, self.DestinyGuardianRankConstantsDefinition,
             self.DestinyLoadoutConstantsDefinition, self.DestinyFireteamFinderConstantsDefinition])


class JsonPaths:

    def __init__(self,
                 en: dict,
                 fr: dict,
                 es: dict,
                 esmx: dict,
                 de: dict,
                 it: dict,
                 ja: dict,
                 ptbr: dict,
                 ru: dict,
                 pl: dict,
                 ko: dict,
                 zhcht: dict,
                 zhchs: dict):
        self.en = DestinyTables.From(en)
        self.fr = DestinyTables.From(fr)
        self.es = DestinyTables.From(es)
        self.esmx = DestinyTables.From(esmx)
        self.de = DestinyTables.From(de)
        self.it = DestinyTables.From(it)
        self.ja = DestinyTables.From(ja)
        self.ptbr = DestinyTables.From(ptbr)
        self.ru = DestinyTables.From(ru)
        self.pl = DestinyTables.From(pl)
        self.ko = DestinyTables.From(ko)
        self.zhcht = DestinyTables.From(zhcht)
        self.zhchs = DestinyTables.From(zhchs)

    @classmethod
    def From(cls, value: dict):
        return cls(
            value['en'],
            value['fr'],
            value['es'],
            value['es-mx'],
            value['de'],
            value['it'],
            value['ja'],
            value['pt-br'],
            value['ru'],
            value['pl'],
            value['ko'],
            value['zh-cht'],
            value['zh-chs']
        )

    def __str__(self):
        return (f'{{"en": "{self.en}", "fr": "{self.fr}", "es": "{self.es}", "es-mx": "{self.esmx}", "de": "{self.de}", "it": "{self.it}", "ja": "{self.ja}", '
                f'"pt-br": "{self.ptbr}", "ru": "{self.ru}", "pl": "{self.pl}", "ko": "{self.ko}", "zh-cht": "{self.zhcht}", "zh-chs": "{self.zhch}" }}')

    def __dict__(self):
        return {
            "en": self.en,
            "fr": self.fr,
            "es": self.es,
            "es-mx": self.esmx,
            "de": self.de,
            "it": self.it,
            "ja": self.ja,
            "pt-br": self.ptbr,
            "ru": self.ru,
            "pl": self.pl,
            "ko": self.ko,
            "zh-cht": self.zhcht,
            "zh-chs": self.zhchs
        }

    def __iter__(self):
        return iter([self.en, self.fr, self.es, self.esmx, self.de, self.it, self.ja, self.ptbr, self.ru, self.pl, self.ko, self.zhcht, self.zhchs])

    def __repr__(self):
        return dumps(self.__dict__(), indent=4)


class MobilePaths:

    def __init__(self,
                 en: str,
                 fr: str,
                 es: str,
                 esmx: str,
                 de: str,
                 it: str,
                 ja: str,
                 ptbr: str,
                 ru: str,
                 pl: str,
                 ko: str,
                 zhcht: str,
                 zhchs: str):
        self.en = en
        self.fr = fr
        self.es = es
        self.esmx = esmx
        self.de = de
        self.it = it
        self.ja = ja
        self.ptbr = ptbr
        self.ru = ru
        self.pl = pl
        self.ko = ko
        self.zhcht = zhcht
        self.zhchs = zhchs

    @classmethod
    def From(cls, value: dict):
        return cls(
            value['en'],
            value['fr'],
            value['es'],
            value['es-mx'],
            value['de'],
            value['it'],
            value['ja'],
            value['pt-br'],
            value['ru'],
            value['pl'],
            value['ko'],
            value['zh-cht'],
            value['zh-chs']
        )

    def __str__(self):
        return (f'{{"en": "{self.en}", "fr": "{self.fr}", "es": "{self.es}", "es-mx": "{self.esmx}", "de": "{self.de}", "it": "{self.it}", "ja": "{self.ja}", '
                f'"pt-br": "{self.ptbr}", "ru": "{self.ru}", "pl": "{self.pl}", "ko": "{self.ko}", "zh-cht": "{self.zhcht}", "zh-chs": "{self.zhch}" }}')

    def __dict__(self):
        return {
            "en": self.en,
            "fr": self.fr,
            "es": self.es,
            "es-mx": self.esmx,
            "de": self.de,
            "it": self.it,
            "ja": self.ja,
            "pt-br": self.ptbr,
            "ru": self.ru,
            "pl": self.pl,
            "ko": self.ko,
            "zh-cht": self.zhcht,
            "zh-chs": self.zhchs
        }

    def __iter__(self):
        return iter([self.en, self.fr, self.es, self.esmx, self.de, self.it, self.ja, self.ptbr, self.ru, self.pl, self.ko, self.zhcht, self.zhchs])

    def __repr__(self):
        return dumps(self.__dict__(), indent=4)


class MobileGearAssets:

    def __init__(self, version: int, path: str):
        self.version = version
        self.path = path

    @classmethod
    def From(cls, value: dict):
        return cls(value['version'], value['path'])

    def __str__(self):
        return f'{{"version": "{self.version}", "path": "{self.path}"}}'

    def __dict__(self):
        return {"version": self.version, "path": self.path}

    def __iter__(self):
        return iter([self.version, self.path])

    def __repr__(self):
        return dumps(self.__dict__(), indent=4)


class MobileGear:

    def __init__(self, Geometry: str, Texture: str, PlateRegion: str, Gear: str, Shader: str):
        self.Geometry = Geometry
        self.Texture = Texture
        self.PlateRegion = PlateRegion
        self.Gear = Gear
        self.Shader = Shader

    @classmethod
    def From(cls, value: dict):
        return cls(value['Geometry'], value['Texture'], value['PlateRegion'], value['Gear'], value['Shader'])

    def __dict__(self):
        return {"Geometry": self.Geometry, "Texture": self.Texture, "PlateRegion": self.PlateRegion, "Gear": self.Gear, "Shader": self.Shader}

    def __str__(self):
        return dumps(self.__dict__())

    def __iter__(self):
        return iter([self.Geometry, self.Texture, self.PlateRegion, self.Gear, self.Shader])

    def __repr__(self):
        return dumps(self.__dict__(), indent=4)


class ManifestResponse:

    def __init__(
            self,
            version: str,
            mobileAssetContentPath: str,
            mobileGearAssetDataBases: list[dict[str, str]],
            mobileWorldContentPaths: dict[str, str],
            jsonWorldContentPaths: dict[str, str],
            jsonWorldComponentContentPaths: dict[str, str],
            mobileClanBannerDatabasePath: str,
            mobileGearCDN: dict[str, str],
            iconImagePyramidInfo: dict[str, str]):
        self.version = version
        self.mobileAssetContentPath = mobileAssetContentPath
        self.mobileGearAssetDataBases = [MobileGearAssets.From(x) for x in mobileGearAssetDataBases]
        self.mobileWorldContentPaths = MobilePaths.From(mobileWorldContentPaths)
        self.jsonWorldContentPaths = MobilePaths.From(jsonWorldContentPaths)
        self.jsonWorldComponentContentPaths = JsonPaths.From(jsonWorldComponentContentPaths)
        self.mobileClanBannerDatabasePath = mobileClanBannerDatabasePath
        self.mobileGearCDN = MobileGear.From(mobileGearCDN)
        self.iconImagePyramidInfo = iconImagePyramidInfo

    @classmethod
    def From(cls, value: dict):
        return cls(
            value['version'],
            value['mobileAssetContentPath'],
            value['mobileGearAssetDataBases'],
            value['mobileWorldContentPaths'],
            value['jsonWorldContentPaths'],
            value['jsonWorldComponentContentPaths'],
            value['mobileClanBannerDatabasePath'],
            value['mobileGearCDN'],
            value['iconImagePyramidInfo']
        )

    def __dict__(self):
        return {
            "version": self.version,
            "mobileAssetContentPath": self.mobileAssetContentPath,
            "mobileGearAssetDataBases": [x.__dict__() for x in self.mobileGearAssetDataBases],
            "mobileWorldContentPaths": self.mobileWorldContentPaths.__dict__(),
            "jsonWorldContentPaths": self.jsonWorldContentPaths.__dict__(),
            "jsonWorldComponentContentPaths": self.jsonWorldComponentContentPaths.__dict__(),
            "mobileClanBannerDatabasePath": self.mobileClanBannerDatabasePath,
            "mobileGearCDN": self.mobileGearCDN.__dict__(),
            "iconImagePyramidInfo": self.iconImagePyramidInfo
        }

    def __str__(self):
        return dumps(self.__dict__())

    def __iter__(self):
        return iter([self.version, self.mobileAssetContentPath, self.mobileGearAssetDataBases, self.mobileWorldContentPaths, self.jsonWorldContentPaths,
                     self.jsonWorldComponentContentPaths, self.mobileClanBannerDatabasePath, self.mobileGearCDN, self.iconImagePyramidInfo])

    def __repr__(self):
        return dumps(self.__dict__(), indent=4)


class Manifest:

    def __init__(self,
                 Response: dict,
                 ErrorCode: int,
                 ThrottleSeconds: int,
                 ErrorStatus: str,
                 Message: str,
                 MessageData: dict[str, str]):
        """
        :type self.Response: ManifestResponse
        """
        self.Response = ManifestResponse.From(Response)
        self.ErrorCode = ErrorCode
        self.ThrottleSeconds = ThrottleSeconds
        self.ErrorStatus = ErrorStatus
        self.Message = Message
        self.MessageData = MessageData

    @classmethod
    def From(cls, value: dict):
        return cls(
            value['Response'],
            value['ErrorCode'],
            value['ThrottleSeconds'],
            value['ErrorStatus'],
            value['Message'],
            value['MessageData']
        )

    def __iter__(self):
        return iter([self.Response, self.ErrorCode, self.ThrottleSeconds, self.ErrorStatus, self.Message, self.MessageData])

    def __dict__(self):
        return {
            "Response": self.Response.__dict__(),
            "ErrorCode": self.ErrorCode,
            "ThrottleSeconds": self.ThrottleSeconds,
            "ErrorStatus": self.ErrorStatus,
            "Message": self.Message,
            "MessageData": self.MessageData
        }

    def __str__(self):
        return dumps(self.__dict__())

    def __repr__(self):
        return dumps(self.__dict__(), indent=4)
