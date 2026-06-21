# Crewbridge Functional Requirements

## Overview

Functional requirements describe what the Crewbridge system must do and the features it must provide to users. These requirements define the core functionality of the platform and support the project objective of connecting hospitality employers with eligible workers through an AI-assisted workforce management system.

---

# 1. Authentication & User Management

| ID   | Requirement                                                               |
| ---- | ------------------------------------------------------------------------- |
| FR-1 | Users shall be able to register using an email address and password.      |
| FR-2 | Users shall be able to log in securely and receive authentication access. |
| FR-3 | Each user shall have a single assigned role.                              |
| FR-4 | The system shall provide role-based access control.                       |
| FR-5 | Users shall be able to view and edit their profile information.           |
| FR-6 | Users shall be able to securely log out.                                  |

---

# 2. Worker Management

| ID    | Requirement                                                                        |
| ----- | ---------------------------------------------------------------------------------- |
| FR-7  | Workers shall be able to create and edit their worker profile.                     |
| FR-8  | Workers shall be able to upload eligibility and employment documents.              |
| FR-9  | Workers shall be able to view their eligibility status.                            |
| FR-10 | Workers shall be able to browse eligible job opportunities.                        |
| FR-11 | Workers shall be able to accept eligible jobs and create placements.               |
| FR-12 | The system shall prevent workers from accepting jobs that exceed work-hour limits. |
| FR-13 | Workers shall be able to view placement history and ratings.                       |

---

# 3. Employer Management

| ID    | Requirement                                                            |
| ----- | ---------------------------------------------------------------------- |
| FR-14 | Employers shall be able to create and manage venue profiles.           |
| FR-15 | Employers shall be able to post staffing requirements.                 |
| FR-16 | Employers shall be able to edit or close job postings.                 |
| FR-17 | Employers shall receive AI-generated worker shortlists.                |
| FR-18 | Employers shall be able to select workers from AI recommendations.     |
| FR-19 | Employers shall be able to rate workers after placement completion.    |
| FR-20 | Employers shall be able to re-book previous workers.                   |
| FR-21 | Employers shall be able to view placement allowances and service fees. |

---

# 4. AI-Assisted Processing

| ID    | Requirement                                                                       |
| ----- | --------------------------------------------------------------------------------- |
| FR-22 | The platform shall provide a centralized AI service module.                       |
| FR-23 | The AI Eligibility Agent shall verify worker eligibility and document compliance. |
| FR-24 | The AI Matching Agent shall rank suitable workers for available jobs.             |
| FR-25 | The AI Screening Agent shall generate skill summaries and suitability scores.     |
| FR-26 | The AI Onboarding Agent shall generate onboarding checklists.                     |
| FR-27 | Low-confidence AI decisions shall be flagged for administrator review.            |

---

# 5. Compliance Management

| ID    | Requirement                                                                            |
| ----- | -------------------------------------------------------------------------------------- |
| FR-28 | The system shall record worker employment conditions and restrictions.                 |
| FR-29 | The system shall prevent placement creation when compliance requirements are breached. |
| FR-30 | The system shall track document expiry dates and notify administrators.                |

---

# 6. Placement & Training

| ID    | Requirement                                                           |
| ----- | --------------------------------------------------------------------- |
| FR-31 | The system shall create placements when workers are accepted.         |
| FR-32 | Placements shall progress through defined status stages.              |
| FR-33 | Trainers shall be assignable to worker inductions.                    |
| FR-34 | The system shall calculate trainer payments for completed inductions. |

---

# 7. Training Marketplace

| ID    | Requirement                                                                               |
| ----- | ----------------------------------------------------------------------------------------- |
| FR-35 | Trainers shall be able to create training material listings.                              |
| FR-36 | Workers shall be able to browse and search training materials.                            |
| FR-37 | Workers shall be able to purchase training materials through a simulated payment process. |
| FR-38 | The system shall track purchases and trainer earnings.                                    |
| FR-39 | Administrators shall be able to review and moderate marketplace listings.                 |

---

# 8. Administration

| ID    | Requirement                                                 |
| ----- | ----------------------------------------------------------- |
| FR-40 | Administrators shall manage user accounts.                  |
| FR-41 | Administrators shall review flagged AI decisions.           |
| FR-42 | Administrators shall access platform analytics and reports. |

---

# 9. Pricing Management

| ID    | Requirement                                                                                |
| ----- | ------------------------------------------------------------------------------------------ |
| FR-43 | The system shall calculate placement allowances and service fees.                          |
| FR-44 | The platform shall display simulated payment information without processing real payments. |

---

# 10. Platform Support

| ID    | Requirement                                                         |
| ----- | ------------------------------------------------------------------- |
| FR-45 | The system shall provide API documentation through Swagger/OpenAPI. |
| FR-46 | The platform shall support synthetic demo data generation.          |

---

## Summary

These functional requirements define the minimum viable product (MVP) functionality for Crewbridge and provide the foundation for development, testing, and deployment activities.
