# FoodRescue — UI and Navigation Structure

## 4.9 UI / Navigation Structure

The FoodRescue user interface shall provide role-specific screens and navigation based on the authenticated user's role.

The interface shall keep common authentication features separate from role-specific operational features.

## 4.9.1 Public Screens

The following screens shall be accessible without authentication:

- Home / Landing Page
- About FoodRescue
- Login
- Registration
- Contact / Support information

## 4.9.2 Common Authenticated Screens

Authenticated users shall have access to:

- Dashboard
- Profile
- Notifications
- Logout

The specific dashboard and available navigation options shall depend on the user's role.

## 4.9.3 Donor Navigation

### Donor Dashboard

Displays:

- Active listings
- Pending requests
- Completed donations
- Expired listings
- Total redistributed quantity
- Recent activity

### Donor Navigation

```text
Dashboard
├── Food Listings
│   ├── View Listings
│   ├── Create Listing
│   └── Listing Details
│
├── Requests
│   ├── Pending Requests
│   └── Request Details
│
├── Donation History
├── Impact Statistics
├── Notifications
└── Profile
```

## 4.9.4 Recipient Navigation

### Recipient Dashboard

Displays:

- Available food
- Pending requests
- Approved requests
- Received food
- Request history

### Recipient Navigation

```
Dashboard
├── Browse Food
│   ├── Search
│   ├── Filters
│   └── Food Details
│
├── My Requests
│   ├── Pending
│   ├── Approved
│   └── History
│
├── Allocations
├── Notifications
└── Profile
```

## 4.9.5 Volunteer Navigation

### Volunteer Dashboard

Displays:

- Assigned tasks
- Pending tasks
- Completed deliveries
- Failed / cancelled tasks

### Volunteer Navigation

```
Dashboard
├── My Assignments
│   ├── Assignment Details
│   ├── Pickup Status
│   └── Delivery Status
│
├── Assignment History
├── Notifications
└── Profile / Availability
```

## 4.9.6 Administrator Navigation

### Administrator Dashboard

Displays:

- Total users
- Active donors, recipients, donors and listings
- Successful redistributions
- Expired food
- Completed deliveries
- Failed transactions
- System activity

### Administrator Navigation

```
Dashboard
├── User Management
│   ├── Donors
│   ├── Recipients
│   └── Volunteers
│
├── Recipient Verification
├── Food Listings
├── Requests & Allocations
├── Pickup & Delivery Monitoring
├── Issues / Disputes
├── Food Categories
├── Reports
├── System Statistics
├── Notifications / Settings
└── Profile
```

## 4.9.7 Main Navigation Flow

The general navigation flow shall be:

```
Landing Page
      ↓
Login / Registration
      ↓
Role-Based Dashboard
      ↓
Role-Specific Functions
      ↓
Transaction / Workflow
      ↓
Status / Notification
      ↓
History / Impact
```

## 4.9.8 UI Design Principles

The interface shall follow these principles:

1. Role-specific navigation
2. Consistent layout and navigation patterns
3. Clear status indicators
4. Clear validation and error messages
5. Minimal unnecessary navigation steps
6. Responsive web layout
7. Clear presentation of food quantity, expiry, location, and availability
8. Consistent terminology throughout the application