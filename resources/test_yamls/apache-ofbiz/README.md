# Apache OFBiz

Physical tables from the Apache OFBiz entity model, as a schema version 4 intermediary.
View-entities are excluded. There is no synthetic cross-cutting column.

## Source

Entity XML commit `5dd66dd617a1fc7435e893a209d9b7ca97827394` under the OFBiz trunk checkout.
Parsed 23 `entitymodel` files. Excluded `framework/entity/entitydef/entitymodel_test.xml`
and the template `framework/resources/templates/entitymodel.xml`.
Excluded 270 `<view-entity>` datasets. `<entity>` and `<extend-entity>` are merged by entity name.
Relations that target a view-entity are not registered, because this catalog has no view datasets.

## Counts

| Measure | Count |
| --- | ---: |
| Entities (datasets) | 835 |
| Columns, including engine stamps | 8694 |
| Logical identities | 835 |
| Entity definitions | 2030 |
| Maximum datasets per identity | 22 |

The maximum is at most 24. Each entity's primary-key identity stays registered on that entity.
A foreign key is registered only when its key-map matches the related entity's primary key
and the related identity would appear on at most 24 datasets.

### Datasets by group

| Group | Datasets |
| --- | ---: |
| `accounting` | 147 |
| `catalina` | 1 |
| `common` | 48 |
| `content` | 64 |
| `entity` | 10 |
| `entityext` | 7 |
| `humanres` | 41 |
| `manufacturing` | 8 |
| `marketing` | 32 |
| `order` | 112 |
| `party` | 84 |
| `product` | 169 |
| `security` | 11 |
| `service` | 10 |
| `shipment` | 35 |
| `webapp` | 14 |
| `webtools` | 1 |
| `workeffort` | 41 |

### Largest identities after the cap

| Identity | Datasets |
| --- | ---: |
| `geo_identity` | 22 |
| `fixed_asset_identity` | 21 |
| `product_category_identity` | 20 |
| `inventory_item_identity` | 19 |
| `invoice_identity` | 17 |
| `shipment_identity` | 16 |
| `agreement_identity` | 15 |
| `custom_method_identity` | 15 |
| `postal_address_identity` | 15 |
| `product_promo_identity` | 15 |
| `cust_request_identity` | 13 |
| `data_resource_identity` | 13 |
| `payment_method_identity` | 13 |
| `product_feature_identity` | 13 |
| `agreement_item_identity` | 12 |

## Unregistered high-fan-out keys

These identities were inferred on more than 24 datasets. Foreign-key definitions were
removed. The primary key of the owning entity remains, so each of these identities is
realized on one dataset. Column names below are the local fields of the dropped foreign keys.
Dropped foreign-key definitions: 968.

| Identity | Would-be datasets | Dropped column names |
| --- | ---: | --- |
| `party_identity` | 153 | `applyingPartyId`, `approverPartyId`, `carrierPartyId`, `clientPartyId`, `committedByPartyId`, `companyPartyId`, `employeePartyId`, `fromPartyId`, `govAgencyPartyId`, `internalPartyId`, `jobIntervieweePartyId`, `jobInterviewerPartyId`, `managerPartyId`, `noteParty`, `organizationPartyId`, `originatedFromPartyId`, `overrideOrgPartyId`, `ownerPartyId`, `partyId`, `partyIdFrom`, `partyIdTo`, `payToPartyId`, `performedByPartyId`, `referredByPartyId`, `supplierPartyId`, `taxAuthPartyId`, `toPartyId`, `vendorPartyId` |
| `status_item_identity` | 74 | `approvalStatusId`, `availabilityStatusId`, `carrierServiceStatusId`, `currentStatusId`, `digitalItemApprovedStatus`, `expectedItemStatus`, `groupStatusId`, `headerApprovedStatus`, `headerCancelStatus`, `headerDeclinedStatus`, `itemApprovedStatus`, `itemCancelStatus`, `itemDeclinedStatus`, `itemStatusId`, `leaveStatus`, `reconcileStatusId`, `runStatusId`, `statusId`, `statusIdTo`, `syncStatusId`, `verifStatusId` |
| `product_identity` | 61 | `instanceOfProductId`, `productId`, `productIdFor`, `productIdIn`, `productIdInSubst`, `productIdTo`, `subProductId` |
| `uom_identity` | 60 | `accountCurrencyUomId`, `actualCurrencyUomId`, `amountUomId`, `availableTimeUomId`, `baseCurrencyUomId`, `billingWeightUomId`, `canclAutmExtTimeUomId`, `costUomId`, `currencyUom`, `currencyUomId`, `defaultCurrencyUomId`, `defaultDimensionUomId`, `defaultUomId`, `defaultWeightUomId`, `depthUomId`, `diameterUomId`, `dimensionUomId`, `elevationUomId`, `facilitySizeUomId`, `gracePeriodOnExpiryUomId`, `heightUomId`, `intervalUomId`, `leadTimeUomId`, `maxLifeTimeUomId`, `maximumAmountUomId`, `meterUomId`, `moneyUomId`, `origCurrencyUomId`, `preferredCurrencyUomId`, `priceUomId`, `quantityUomId`, `rateCurrencyUomId`, `recurringFreqUomId`, `termUomId`, `totalCubicUomId`, `totalWeightUomId`, `uomId`, `uomIdTo`, `useTimeUomId`, `weightUomId`, `widthUomId` |
| `user_login_identity` | 56 | `approvedByUserLoginId`, `assignedByUserLoginId`, `authUserLoginId`, `changeByUserLoginId`, `changeUserLogin`, `changeUserLoginId`, `changedByUserLogin`, `createdBy`, `createdByUserLogin`, `createdByUserLoginId`, `dontCancelSetUserLogin`, `issuedByUserLoginId`, `lastModifiedByUserLogin`, `modifiedByUserLogin`, `modifiedByUserLoginId`, `originUserLoginId`, `receivedByUserLoginId`, `runAsUser`, `runByUserLoginId`, `setByUserLogin`, `statusUserLogin`, `userLoginId` |
| `party_role_identity` | 54 | `carrierPartyId`, `carrierRoleTypeId`, `employeePartyId`, `employeeRoleTypeId`, `managerPartyId`, `managerRoleTypeId`, `organizationPartyId`, `originatedFromPartyId`, `originatedFromRoleTypeId`, `partyId`, `partyIdFrom`, `partyIdTo`, `roleTypeId`, `roleTypeIdFrom`, `roleTypeIdTo` |
| `role_type_identity` | 49 | `originatedFromRoleTypeId`, `parentTypeId`, `roleTypeId`, `roleTypeIdFrom`, `roleTypeIdTo`, `roleTypeIdValidFrom`, `roleTypeIdValidTo`, `useRoleTypeId` |
| `enumeration_identity` | 48 | `changeTypeEnumId`, `classEnumId`, `cogsMethodId`, `creditCardEnumId`, `defaultSalesChannelEnumId`, `delegateReasonEnumId`, `emailType`, `employmentStatusEnumId`, `examTypeEnumId`, `expectationEnumId`, `geoPointTypeEnumId`, `gradeSecuredEnumId`, `inputParamEnumId`, `jobPostingTypeEnumId`, `keywordTypeId`, `linkTypeEnumId`, `locationTypeEnumId`, `operatorEnumId`, `paymentServiceTypeEnumId`, `planMethodEnumId`, `privilegeEnumId`, `productGeoEnumId`, `productPromoActionEnumId`, `productPromoApplEnumId`, `purposeEnumId`, `ratingTypeEnum`, `reasonEnumId`, `relationshipEnumId`, `replenishEnumId`, `replenishMethodEnumId`, `requirementMethodEnumId`, `reserveOrderEnumId`, `residenceStatusEnumId`, `resourceTypeEnumId`, `salesChannelEnumId`, `scopeEnumId`, `sourceEnumId`, `storeCreditAccountEnumId`, `targetTypeEnumId`, `taxFormId`, `telecomMsgTypeEnumId`, `transCodeEnumId`, `typeEnumId`, `virtualVariantMethodEnum` |
| `order_header_identity` | 47 | `acquireOrderId`, `engagementId`, `orderId`, `primaryOrderId`, `purchaseOrderId`, `replacementOrderId`, `toOrderId` |
| `work_effort_identity` | 45 | `estimatedArrivalWorkEffId`, `estimatedShipWorkEffId`, `maintTemplateWorkEffortId`, `processWorkEffortId`, `routingWorkEffortId`, `scheduleWorkEffortId`, `workEffortId`, `workEffortIdFrom`, `workEffortIdTo`, `workEffortParentId` |
| `contact_mech_identity` | 37 | `contactMechId`, `contactMechIdFrom`, `contactMechIdTo`, `destContactMechId`, `destinationContactMechId`, `fulfillContactMechId`, `originContactMechId`, `preferredContactMechId`, `telecomContactMechId` |
| `facility_identity` | 37 | `destFacilityId`, `destinationFacilityId`, `facilityId`, `facilityIdTo`, `inventoryFacilityId`, `locatedAtFacilityId`, `originFacilityId`, `parentFacilityId` |
| `order_item_identity` | 31 | `acquireOrderId`, `acquireOrderItemSeqId`, `engagementId`, `engagementItemSeqId`, `orderId`, `orderItemSeqId`, `toOrderId`, `toOrderItemSeqId` |
| `content_identity` | 30 | `contentId`, `contentIdTo`, `decoratorContentId`, `helpContentId`, `instanceOfContentId`, `ownerContentId` |
| `gl_account_identity` | 30 | `accDepGlAccountId`, `assetGlAccountId`, `defaultGlAccountId`, `depGlAccountId`, `glAccountId`, `lossGlAccountId`, `overrideGlAccountId`, `parentGlAccountId`, `postToGlAccountId`, `profitGlAccountId` |
| `product_store_identity` | 25 | `productStoreId` |

## Stamp columns

`ModelEntity` injects `lastUpdatedStamp`, `lastUpdatedTxStamp`, `createdStamp`, and
`createdTxStamp` as `date-time` columns unless `no-auto-stamp` is set.
With `no-auto-stamp` and `enable-lock`, only `lastUpdatedStamp` and `createdStamp` are injected.
A stamp the entity already declares is not duplicated. Stamp columns are not a logical entity.
Entities with all four stamps: 832.
Entities with no engine stamps: 3.
Entities with only the two lock stamps: 0.

## Memory loss

Configuration `memory-loss-v1` applied to domain `apache-ofbiz`. Each decision is
`sha256(name + domain + path + kind)`. Structural fields are unchanged:
identifiers, names, accessors, column names, and `dataset_columns`.
A `complete` entity universe is never left with `conforms: false`.

| Kind | Rate | Eligible | Forgotten |
| --- | ---: | ---: | ---: |
| `description` | 0.08 | 13162 | 1082 |
| `synonyms` | 0.15 | 1640 | 241 |
| `tags` | 0.15 | 835 | 119 |
| `value_description` | 0.12 | 8694 | 1065 |
| `entity_expression` | 0.1 | 2030 | 195 |
| `entity_metadata` | 0.1 | 2030 | 233 |
| `grain_component_description` | 0.08 | 768 | 58 |
| `grain` | 0.06 | 835 | 67 |
| `grain_component_identity` | 0.05 | 768 | 37 |
| `claim` | 0.07 | 7487 | 528 |

Every kind that had eligible values has a non-zero forgotten count.
Grain-component descriptions are the sentence `Primary key of <entity>`.
`forget-log.yaml` lists every forgotten path and its original value.

## Files

| Path | Contents |
| --- | --- |
| `directory-manifest.yaml` | Schema version 4 directory manifest. Paths are relative to `yaml/`. |
| `yaml/00_logical_identities.yaml` | `schema_version` and `logical_identities` only. |
| `yaml/<group>.yaml` | `schema_version` and `nodes` for one entity group. |
| `forget-log.yaml` | Rate table, counts by kind, and every forgotten value. |
| `questions.md` | Operator questions over orders, inventory, accounting, manufacturing, and shipments. |
