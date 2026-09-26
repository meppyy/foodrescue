# FoodRescue — API and Backend Design

## 4.8 API / Backend Design

The FoodRescue backend will be implemented using Python Flask and will expose HTTP-based endpoints through which the frontend communicates with the application.

The backend will use a modular route and service structure. Routes will handle incoming HTTP requests and responses, while business logic will be delegated to appropriate service components.

## 4.8.1 Backend Request Flow

A typical backend request will follow this sequence:

1. Client sends an HTTP request.
2. Flask receives the request through the appropriate route.
3. Authentication and authorization are checked where required.
4. Input data is validated.
5. The appropriate business service is called.
6. The service performs required business logic.
7. SQLAlchemy performs database operations where required.
8. MySQL stores or retrieves persistent data.
9. The backend returns a structured response to the client.

## 4.8.2 API Design Principles

The API shall:

- Use HTTP methods according to the operation being performed.
- Use meaningful resource-oriented URLs.
- Require authentication for protected resources.
- Enforce role-based authorization.
- Validate incoming data.
- Return appropriate HTTP status codes.
- Return consistent response structures.
- Prevent unauthorized access to other users' resources.
- Keep business logic inside service components rather than route functions where practical.

## 4.8.3 Authentication APIs

| Method | Endpoint | Access | Purpose |
|---|---|---|---|
| POST | `/api/auth/register` | Public | Register a new user |
| POST | `/api/auth/login` | Public | Authenticate a user |
| POST | `/api/auth/logout` | Authenticated | Log out the current user |
| GET | `/api/users/me` | Authenticated | Get current user profile |
| PATCH | `/api/users/me` | Authenticated | Update current user profile |

## 4.8.4 Food Listing APIs

| Method | Endpoint | Access | Purpose |
|---|---|---|---|
| GET | `/api/listings` | Recipient / Admin | Get available food listings |
| POST | `/api/listings` | Donor | Create a food listing |
| GET | `/api/listings/{listing_id}` | Authorized | Get listing details |
| PATCH | `/api/listings/{listing_id}` | Donor | Update an eligible listing |
| PATCH | `/api/listings/{listing_id}/cancel` | Donor | Cancel an available listing |

## 4.8.5 Search and Filtering APIs

The food-listing endpoint shall support query parameters for searching, filtering, and sorting.

Example:

`GET /api/listings?category=prepared-food&dietary_type=vegetarian&sort=expiry`

Supported query parameters may include:

- `search`
- `category`
- `dietary_type`
- `quantity`
- `location`
- `distance`
- `priority`
- `status`
- `listed_after`
- `sort`

Sorting options may include:

- `expiry`
- `distance`
- `quantity`
- `newest`

## 4.8.6 Recipient Matching and Prioritization

Prioritization and recipient matching shall primarily be implemented as backend business services rather than requiring separate public APIs.

The relevant services will include:

- `PrioritizationService`
- `MatchingService`

The prioritization service will calculate food priority using the defined rule-based factors.

The matching service will identify and rank suitable recipients using the defined eligibility and compatibility criteria.

These services may be called internally when listings are created, updated, searched, or processed.

## 4.8.7 Food Request APIs

| Method | Endpoint | Access | Purpose |
|---|---|---|---|
| POST | `/api/listings/{listing_id}/requests` | Recipient | Request food |
| GET | `/api/requests` | Authenticated | View relevant requests |
| GET | `/api/requests/{request_id}` | Authorized | View request details |
| PATCH | `/api/requests/{request_id}/approve` | Donor / Admin | Approve request |
| PATCH | `/api/requests/{request_id}/reject` | Donor / Admin | Reject request |
| PATCH | `/api/requests/{request_id}/cancel` | Recipient | Cancel eligible request |

## 4.8.8 Allocation APIs

| Method | Endpoint | Access | Purpose |
|---|---|---|---|
| GET | `/api/allocations` | Authorized | View relevant allocations |
| GET | `/api/allocations/{allocation_id}` | Authorized | View allocation details |
| POST | `/api/requests/{request_id}/allocation` | System / Authorized | Create allocation from approved request |
| PATCH | `/api/allocations/{allocation_id}/cancel` | Authorized | Cancel allocation |

Allocation creation shall validate request approval and available food quantity before the allocation is created.

## 4.8.9 Volunteer and Delivery APIs

| Method | Endpoint | Access | Purpose |
|---|---|---|---|
| GET | `/api/assignments` | Volunteer | View volunteer assignments |
| GET | `/api/assignments/{allocation_id}` | Volunteer / Admin | View assignment details |
| PATCH | `/api/assignments/{allocation_id}/accept` | Volunteer | Accept assignment |
| PATCH | `/api/assignments/{allocation_id}/reject` | Volunteer | Reject assignment |
| PATCH | `/api/assignments/{allocation_id}/pickup` | Volunteer | Update pickup status |
| PATCH | `/api/assignments/{allocation_id}/delivery` | Volunteer | Update delivery status |
| POST | `/api/allocations/{allocation_id}/receipt` | Recipient | Confirm receipt |

The backend shall enforce the rule that delivery cannot be marked complete before pickup has been confirmed.

## 4.8.10 Notification APIs

| Method | Endpoint | Access | Purpose |
|---|---|---|---|
| GET | `/api/notifications` | Authenticated | Get user's notifications |
| PATCH | `/api/notifications/{notification_id}/read` | Authenticated | Mark notification as read |

Notifications will also be generated internally by workflow services when relevant events occur.

## 4.8.11 Dashboard APIs

| Method | Endpoint | Access | Purpose |
|---|---|---|---|
| GET | `/api/dashboard/donor` | Donor | Donor dashboard data |
| GET | `/api/dashboard/recipient` | Recipient | Recipient dashboard data |
| GET | `/api/dashboard/volunteer` | Volunteer | Volunteer dashboard data |
| GET | `/api/dashboard/admin` | Administrator | Administrator dashboard data |

Dashboard responses shall contain information relevant to the authenticated user's role.

## 4.8.12 Administration APIs

| Method | Endpoint | Access | Purpose |
|---|---|---|---|
| GET | `/api/admin/users` | Admin | View users |
| PATCH | `/api/admin/users/{user_id}` | Admin | Manage user account |
| GET | `/api/admin/recipients/pending` | Admin | View pending recipient verifications |
| PATCH | `/api/admin/recipients/{recipient_id}/approve` | Admin | Approve recipient |
| PATCH | `/api/admin/recipients/{recipient_id}/reject` | Admin | Reject recipient |
| DELETE | `/api/admin/listings/{listing_id}` | Admin | Remove invalid listing |
| GET | `/api/admin/requests` | Admin | Monitor requests |
| GET | `/api/admin/allocations` | Admin | Monitor allocations |
| GET | `/api/admin/reports` | Admin | View system reports |
| GET | `/api/admin/statistics` | Admin | View system statistics |

## 4.8.13 HTTP Status Codes

The backend shall use appropriate HTTP status codes.

| Status | Meaning |
|---|---|
| 200 | Request successful |
| 201 | Resource successfully created |
| 204 | Successful operation with no response body |
| 400 | Invalid request |
| 401 | Authentication required |
| 403 | Access forbidden |
| 404 | Resource not found |
| 409 | Resource or state conflict |
| 422 | Validation failure |
| 500 | Unexpected server error |

## 4.8.14 Standard Response Structure

Successful responses should follow a consistent structure.

Example:

```json
{
    "status": "success",
    "message": "Food listing created successfully",
    "data": {
        "listing_id": 101
    }
}
```

Error responses should follow a consistent structure.

Example: 
```
{
    "status": "error",
    "message": "Requested quantity exceeds available quantity",
    "error_code": "INSUFFICIENT_QUANTITY"
}
```

## 4.8.15 Backend Module Structure

The Flask backend shall be organized into separate route, service, model, configuration, and extension components.

Proposed structure:

```
backend/
    └── app/
        ├── init.py
        ├── config.py
        ├── extensions.py
        ├── models/
            ├── user.py
            ├── donor.py
            ├── recipient.py
            ├── volunteer.py
            ├── food_listing.py
            ├── food_request.py
            ├── allocation.py
            └── notification.py
        ├── routes/
            ├── auth.py
            ├── listings.py
            ├── requests.py
            ├── allocations.py
            ├── delivery.py
            ├── notifications.py
            ├── dashboard.py
            └── admin.py
        └── services/
            ├── authentication.py
            ├── food_listing.py
            ├── prioritization.py
            ├── matching.py
            ├── request_allocation.py
            ├── delivery.py
            ├── expiry.py
            ├── notification.py
            └── impact.py
```

## 4.8.16 Business Logic Separation

Route functions shall primarily handle:

- Receiving requests
- Authentication checks
- Input validation
- Calling services
- Returning responses

Business services shall handle:

- Prioritization
- Recipient matching
- Request validation
- Allocation rules
- Delivery workflow
- Expiry processing
- Notification generation
- Impact calculations

Database models shall represent persistent system entities and relationships.