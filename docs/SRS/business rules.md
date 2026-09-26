# FoodRescue — Business Rules

## 2.3 Business Rules

### 2.3.1 User and Access Rules

BR-USER-01: Only authenticated users shall access protected system functionality.

BR-USER-02: Users shall only access functionality permitted by their assigned role.

BR-USER-03: Only approved recipients shall be permitted to request surplus food.

BR-USER-04: Administrative functionality shall be restricted to authorized administrators.

### 2.3.2 Food Listing Rules

BR-FOOD-01: A food listing shall contain the required information before it can become available.

BR-FOOD-02: Expired food shall not be available for new requests.

BR-FOOD-03: Cancelled food listings shall not receive new requests.

BR-FOOD-04: A donor may cancel an available listing before the listing has been allocated.

BR-FOOD-05: The quantity available for a food listing shall be maintained throughout the request and allocation workflow.

### 2.3.3 Request Rules

BR-REQ-01: A recipient shall not request more food than the currently available quantity.

BR-REQ-02: A request shall not be created for expired or unavailable food.

BR-REQ-03: A request shall remain subject to approval or rejection by an authorized user.

BR-REQ-04: A request shall only proceed to allocation after approval.

BR-REQ-05: A cancelled, rejected, or expired request shall not proceed to a new allocation.

### 2.3.4 Allocation Rules

BR-ALLOC-01: An allocation shall be created only from an approved request.

BR-ALLOC-02: The total quantity allocated shall not exceed the available quantity of the corresponding food listing.

BR-ALLOC-03: The same available food quantity shall not be allocated to multiple recipients beyond the available amount.

BR-ALLOC-04: Completed transactions shall not be arbitrarily modified by ordinary users.

### 2.3.5 Volunteer and Delivery Rules

BR-DEL-01: A volunteer shall only receive assignments that are available for assignment to that volunteer.

BR-DEL-02: A volunteer assignment shall be associated with an approved allocation.

BR-DEL-03: Delivery shall not be marked as completed before pickup has been confirmed.

BR-DEL-04: A cancelled or failed assignment shall not remain in an active completed-delivery state.

BR-DEL-05: If an assigned volunteer becomes unavailable, the assignment may be returned to an unassigned state for reassignment.

### 2.3.6 Expiry Rules

BR-EXP-01: The system shall compare the current time with the expiry time of active food listings.

BR-EXP-02: A listing whose expiry time has passed shall be marked as expired.

BR-EXP-03: Expired listings shall not accept new requests.

BR-EXP-04: Pending requests affected by food expiry shall be handled according to the expiry workflow and may be automatically cancelled.

### 2.3.7 Prioritization and Matching Rules

BR-SMART-01: Food prioritization shall use predefined rule-based criteria.

BR-SMART-02: Priority calculation may consider expiry urgency, quantity, food category, distance, recipient suitability, and listing age.

BR-SMART-03: Food listings shall be classified as High, Medium, or Low Priority.

BR-MATCH-01: Recipient matching shall consider eligibility before a recipient is considered a suitable match.

BR-MATCH-02: Recipient matching may consider food type, dietary compatibility, required quantity, recipient capacity, geographic proximity, availability, and expiry urgency.

BR-MATCH-03: Recipients that fail mandatory eligibility or compatibility requirements shall not be considered suitable matches.

### 2.3.8 Data and Workflow Rules

BR-DATA-01: Important state changes shall be recorded in the system.

BR-DATA-02: Food availability, request, allocation, pickup, and delivery states shall remain consistent throughout the workflow.

BR-DATA-03: A completed redistribution transaction shall contribute to the relevant impact statistics.

BR-DATA-04: System-generated notifications shall be associated with the relevant user and event.