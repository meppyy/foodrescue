# FoodRescue — Requirements Traceability

## 2.7 Requirements Traceability

The Requirements Traceability Matrix (RTM) establishes a relationship between the major system requirements, corresponding use cases, planned system design components, implementation modules, and test cases.

The matrix will be maintained throughout development so that changes to requirements can be reflected consistently across system design, implementation, and testing.

## 2.7.1 Requirements Traceability Matrix

| Requirement ID | Requirement Area | Related Use Case(s) | Design / Module | Test Case |
|---|---|---|---|---|
| FR-AUTH-01 | User Registration | UC-D01, UC-R01, UC-V01 | Authentication Module | TC-AUTH-01 |
| FR-AUTH-05 | User Login | UC-D02, UC-R02, UC-V02, UC-A01 | Authentication Module | TC-AUTH-02 |
| FR-AUTH-09 | Role-Based Access | Multiple role-specific use cases | Authorization Module | TC-AUTH-03 |
| FR-AUTH-17 | Recipient Verification | UC-A03 | Administration Module | TC-AUTH-04 |
| FR-FOOD-01 | Create Food Listing | UC-D04 | Food Listing Module | TC-FOOD-01 |
| FR-FOOD-08 | Specify Expiry Time | UC-D04 | Food Listing Module | TC-FOOD-02 |
| FR-FOOD-16 | View Active Listings | UC-D07 | Food Listing Module | TC-FOOD-03 |
| FR-FOOD-18 | Cancel Food Listing | UC-D06 | Food Listing Module | TC-FOOD-04 |
| FR-SEARCH-01 | Browse Available Food | UC-R04 | Search Module | TC-SEARCH-01 |
| FR-SEARCH-06 | Filter by Category | UC-R06 | Search Module | TC-SEARCH-02 |
| FR-SEARCH-13 | Sort by Expiry | UC-R06 | Search Module | TC-SEARCH-03 |
| FR-PRIORITY-01 | Calculate Food Priority | — | Prioritization Module | TC-PRIORITY-01 |
| FR-PRIORITY-08 | Priority Classification | — | Prioritization Module | TC-PRIORITY-02 |
| FR-MATCH-01 | Identify Eligible Recipients | — | Matching Module | TC-MATCH-01 |
| FR-MATCH-10 | Rank Suitable Recipients | — | Matching Module | TC-MATCH-02 |
| FR-REQUEST-01 | Submit Food Request | UC-R08 | Request Module | TC-REQUEST-01 |
| FR-REQUEST-09 | Approve Request | UC-D09 / UC-A08 | Request Module | TC-REQUEST-02 |
| FR-REQUEST-15 | Create Allocation | — | Allocation Module | TC-REQUEST-03 |
| FR-DELIVERY-01 | Assign Volunteer | — | Delivery Module | TC-DELIVERY-01 |
| FR-DELIVERY-09 | Confirm Pickup | UC-V09 | Delivery Module | TC-DELIVERY-02 |
| FR-DELIVERY-12 | Confirm Delivery | UC-V12 | Delivery Module | TC-DELIVERY-03 |
| FR-DELIVERY-17 | Prevent Delivery Before Pickup | — | Delivery Validation | TC-DELIVERY-04 |
| FR-EXPIRY-02 | Check Expiry | — | Expiry Management Module | TC-EXPIRY-01 |
| FR-EXPIRY-09 | Mark Listing Expired | — | Expiry Management Module | TC-EXPIRY-02 |
| FR-EXPIRY-10 | Prevent Requests for Expired Food | — | Expiry Management Module | TC-EXPIRY-03 |
| FR-NOTIFY-01 | Generate Notifications | Various workflow use cases | Notification Module | TC-NOTIFY-01 |
| FR-DASH-01 | Donor Dashboard | — | Dashboard Module | TC-DASH-01 |
| FR-DASH-16 | Admin Dashboard | — | Dashboard Module | TC-DASH-02 |
| FR-IMPACT-01 | Track Food Listed | — | Impact Tracking Module | TC-IMPACT-01 |
| FR-IMPACT-02 | Track Food Redistributed | — | Impact Tracking Module | TC-IMPACT-02 |
| FR-ADMIN-01 | Manage Users | UC-A02 | Administration Module | TC-ADMIN-01 |
| FR-ADMIN-06 | Verify Recipients | UC-A03 | Administration Module | TC-ADMIN-02 |
| FR-ADMIN-10 | Monitor Food Listings | UC-A06 | Administration Module | TC-ADMIN-03 |

## 2.7.2 Traceability Maintenance

The Requirements Traceability Matrix shall be updated whenever a major requirement is added, removed, modified, or replaced.

Changes to a requirement shall be reviewed for their effect on:

- Related use cases
- System design
- Database structure
- Application modules
- Test cases
- Project documentation

The final traceability matrix will be expanded during system design, implementation, and testing to include all finalized requirements and their corresponding artifacts.