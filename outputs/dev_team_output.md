# Development Team Report

## Product Manager

## Product Requirements Document (PRD)

**Product Name:** EduBridge

### 1. Product Vision

To create an intuitive and efficient web-based platform that streamlines the assignment submission, grading, and course management processes for academic institutions. EduBridge aims to enhance collaboration between students and teachers, simplify administrative tasks, and provide a clear overview of academic progress. Our long-term vision is to foster an engaging and productive learning environment through technology.

### 2. Target Users

The primary target users for EduBridge are:

*   **Students:** Individuals enrolled in courses who need to submit assignments and track their academic progress.
*   **Teachers (Instructors/Professors):** Educators responsible for creating course content, managing assignments, reviewing student work, and issuing grades.
*   **Administrators:** Staff responsible for managing user accounts, courses, and overall system configuration.

### 3. MVP Features

The Minimum Viable Product (MVP) of EduBridge will focus on the core functionalities requested, ensuring a functional and valuable initial release.

#### 3.1. Student Module

*   **Assignment Submission:** Students can upload files for specific assignments.
*   **Grade Viewing:** Students can view the grades and feedback for their submitted assignments.

#### 3.2. Teacher Module

*   **Course Creation & Management:** Teachers can create, edit, and manage their courses.
*   **Assignment Management:** Teachers can create, edit, and publish assignments within their courses.
*   **Assignment Review & Grading:** Teachers can access student submissions, provide feedback, and assign grades.

#### 3.3. Administrator Module

*   **User Management:** Administrators can create, view, edit, and delete user accounts (Students, Teachers, Administrators).

#### 3.4. Core Platform Features

*   **User Authentication:** Secure login and logout functionality for all user roles.
*   **Role-Based Access Control:** Ensure users only have access to features relevant to their assigned role.

### 4. Functional Requirements

#### 4.1. General Platform Requirements

*   **FR-001:** The system shall allow users to register and log in securely.
*   **FR-002:** The system shall differentiate user permissions based on assigned roles (Student, Teacher, Administrator).
*   **FR-003:** The system shall display a dashboard or home page relevant to the logged-in user's role.

#### 4.2. Student Module Requirements

*   **FR-S-001:** Students shall be able to view a list of courses they are enrolled in.
*   **FR-S-002:** Students shall be able to view a list of assignments for each course, including due dates and submission status.
*   **FR-S-003:** Students shall be able to upload a file (e.g., PDF, DOCX, JPG) as an assignment submission.
*   **FR-S-004:** The system shall allow students to resubmit assignments if the deadline has not passed and the teacher allows it.
*   **FR-S-005:** Students shall be able to view their assigned grade and any associated feedback for each submitted assignment.
*   **FR-S-006:** Students shall be able to view their overall grade for a course (e.g., sum/average of assignment grades).

#### 4.3. Teacher Module Requirements

*   **FR-T-001:** Teachers shall be able to create a new course, specifying a course name, description, and academic term/year.
*   **FR-T-002:** Teachers shall be able to edit course details.
*   **FR-T-003:** Teachers shall be able to view a list of all courses they are assigned to.
*   **FR-T-004:** Teachers shall be able to add new assignments within a specific course, including title, description, due date, and allowed submission file types.
*   **FR-T-005:** Teachers shall be able to view a list of all submitted assignments for a given assignment.
*   **FR-T-006:** Teachers shall be able to download individual student assignment submissions.
*   **FR-T-007:** Teachers shall be able to provide textual feedback and assign a numerical or letter grade for each student submission.
*   **FR-T-008:** Teachers shall be able to publish grades and feedback to students, making them visible.
*   **FR-T-009:** Teachers shall be able to view a gradebook for each course, showing all students and their assignment grades.

#### 4.4. Administrator Module Requirements

*   **FR-A-001:** Administrators shall be able to create new user accounts, specifying username, password, email, and user role (Student, Teacher, Administrator).
*   **FR-A-002:** Administrators shall be able to view a list of all registered users.
*   **FR-A-003:** Administrators shall be able to edit existing user account details, including role assignment.
*   **FR-A-004:** Administrators shall be able to delete user accounts.
*   **FR-A-005:** Administrators shall be able to enroll students in courses and assign teachers to courses.

### 5. Non-Functional Requirements

*   **Performance (NFR-P):**
    *   **NFR-P-001:** The platform shall load pages within 3 seconds for 90% of users under normal load conditions.
    *   **NFR-P-002:** Assignment uploads up to 100MB shall complete within 30 seconds under normal network conditions.
*   **Security (NFR-S):**
    *   **NFR-S-001:** All data transmission between the client and server shall be encrypted using industry-standard protocols (e.g., HTTPS).
    *   **NFR-S-002:** User passwords shall be securely hashed and salted.
    *   **NFR-S-003:** The system shall implement robust authentication and authorization mechanisms to prevent unauthorized access to data and functionalities.
    *   **NFR-S-004:** The platform shall be protected against common web vulnerabilities (e.g., SQL injection, XSS).
*   **Usability (NFR-U):**
    *   **NFR-U-001:** The user interface shall be intuitive and easy to navigate for all user roles.
    *   **NFR-U-002:** The platform shall provide clear error messages and guidance for users.
    *   **NFR-U-003:** The design shall be responsive, ensuring a consistent experience across various devices (desktop, tablet, mobile).
*   **Reliability (NFR-R):**
    *   **NFR-R-001:** The system shall have an uptime of 99.5% excluding scheduled maintenance.
    *   **NFR-R-002:** All critical data shall be backed up daily with a retention period of at least 30 days.
*   **Scalability (NFR-SC):**
    *   **NFR-SC-001:** The platform architecture shall be designed to support up to 5,000 active users concurrently without significant performance degradation.
*   **Maintainability (NFR-M):**
    *   **NFR-M-001:** The codebase shall be well-documented and follow established coding standards to facilitate future updates and maintenance.

### 6. Open Assumptions

*   **Platform Scope:** The platform is initially assumed to be a standalone system, with no integration required for existing Student Information Systems (SIS) or Learning Management Systems (LMS).
*   **Assignment Types:** For MVP, assignments are primarily file uploads. Text-entry assignments, quizzes, or other interactive assignment types are out of scope.
*   **Communication:** No internal messaging system, announcement board, or discussion forums are included in the MVP.
*   **Notifications:** Grade notifications are assumed to be visible within the platform only, not via email or external channels in MVP.
*   **Course Enrollment:** Administrators are responsible for enrolling students into courses and assigning teachers to courses. There is no self-enrollment feature for students or direct course assignment for teachers in MVP.
*   **File Storage:** A solution for secure and scalable file storage (e.g., cloud storage) is assumed to be in place.
*   **Feedback Mechanism:** Feedback is assumed to be textual comments alongside a grade. Richer feedback types (e.g., inline annotation, audio feedback) are out of scope for MVP.
*   **Grade Calculation:** Basic grade calculation (e.g., sum, average) is assumed for overall course grades. Complex grading schemes, weighting, or rubrics are out of scope for MVP.
*   **Authentication Method:** Standard username/password authentication is assumed for MVP. Single Sign-On (SSO) or OAuth integrations are out of scope.

---

## Architect

## Technical Architecture for EduBridge

Based on the provided Product Requirements Document (PRD), this document outlines a concrete technical architecture for the EduBridge platform, focusing on the MVP features and requirements while considering future scalability and maintainability.

---

### 1. Recommended Tech Stack

To meet the requirements for a web-based, intuitive, and scalable platform with efficient development for MVP, the following tech stack is recommended:

*   **Frontend:** **React.js** (or Vue.js/Angular) for building a responsive, dynamic, and maintainable single-page application (SPA).
    *   **Libraries:** Modern UI component library (e.g., Material-UI, Ant Design) for rapid development and consistent UI/UX (NFR-U-001, NFR-U-003).
*   **Backend:** **Python with Django REST Framework** for robust API development, built-in ORM, admin panel for initial management, and strong security features.
    *   **Alternatives:** Node.js with Express, Java with Spring Boot, or Ruby on Rails could also be viable. Django offers a good balance of rapid development and comprehensive features suitable for MVP.
*   **Database:** **PostgreSQL** for relational data storage. It's a powerful, open-source, and highly reliable SQL database, suitable for structured data like users, courses, assignments, and grades, and supports scalability needs.
*   **File Storage:** **Amazon S3** (or Google Cloud Storage/Azure Blob Storage) for scalable and secure storage of assignment submission files. This offloads file management from the backend application servers and offers high durability and availability.
*   **Authentication & Authorization:** **JSON Web Tokens (JWT)** for stateless session management combined with a robust Role-Based Access Control (RBAC) system implemented in the backend.

### 2. System Components

The EduBridge platform will be composed of a client application interacting with a set of backend services, supported by dedicated data and file storage.

1.  **Client Application (Frontend):**
    *   A web-based SPA developed with React.js, responsible for rendering the user interface for Students, Teachers, and Administrators.
    *   Interacts with the Backend API using AJAX requests.
    *   Handles user authentication state and redirects based on roles (FR-003).

2.  **API Gateway / Load Balancer:**
    *   Acts as the single entry point for all client requests.
    *   Distributes incoming traffic across multiple backend service instances to ensure high availability and scalability (NFR-SC-001).
    *   Handles SSL/TLS termination (NFR-S-001).

3.  **Backend Services (Logical Separation, initially deployed as a Monolith or Modular Monolith):**
    *   **User & Authentication Service:** Manages user registration (FR-A-001), login/logout (FR-001), password hashing (NFR-S-002), user roles (FR-002), and JWT token generation/validation. Handles user CRUD (FR-A-001, FR-A-002, FR-A-003, FR-A-004).
    *   **Course & Enrollment Service:** Handles course creation/management (FR-T-001, FR-T-002, FR-T-003), student enrollment (FR-A-005), and teacher assignment to courses (FR-A-005).
    *   **Assignment Management Service:** Manages assignment creation/editing (FR-T-004), viewing assignment lists (FR-S-002), and their details.
    *   **Submission Service:** Manages assignment file uploads (FR-S-003), resubmissions (FR-S-004), tracks submission status, and integrates with the File Storage system. Provides download functionality for teachers (FR-T-006).
    *   **Grading & Feedback Service:** Stores and retrieves grades (FR-S-005, FR-T-007) and feedback (FR-S-005, FR-T-007). Manages grade visibility (FR-T-008) and calculates overall course grades (FR-S-006, FR-T-009).

4.  **Database:**
    *   A PostgreSQL instance storing all structured application data (users, roles, courses, assignments, submission metadata, grades, feedback).

5.  **File Storage:**
    *   An Amazon S3 bucket (or equivalent) for storing all uploaded assignment files.

### 3. Data Storage Approach

*   **Relational Database (PostgreSQL):**
    *   **Purpose:** Stores all structured, transactional data critical to the application's functionality. This includes:
        *   User information (username, email, hashed password, role, etc.)
        *   Course details (name, description, term, etc.)
        *   Assignment details (title, description, due date, allowed file types)
        *   Student enrollment in courses
        *   Teacher assignments to courses
        *   Assignment submission metadata (who submitted, when, file reference, status)
        *   Grades and associated textual feedback
    *   **Schema Design:** Will incorporate appropriate foreign keys and indices to ensure data integrity and efficient querying.
    *   **Backup Strategy:** Daily automated backups with a 30-day retention period (NFR-R-002).

*   **Object Storage (Amazon S3):**
    *   **Purpose:** Stores the actual binary files uploaded by students for assignments (e.g., PDF, DOCX, JPG).
    *   **Naming Convention:** Files will be stored with unique, non-guessable keys, potentially incorporating user ID and assignment ID for organization and security.
    *   **Access Control:** Access to files will be controlled by pre-signed URLs generated by the backend, ensuring that only authorized users (teachers) can download submissions and students can only access their own submitted files.

### 4. API Style

*   **RESTful API:** The backend will expose a RESTful API, providing a clear, stateless, and resource-oriented interface for the frontend application.
    *   **HTTP Methods:** Utilizes standard HTTP methods (GET, POST, PUT, DELETE) for performing CRUD operations on resources (e.g., `/api/courses`, `/api/assignments/{id}/submissions`).
    *   **Data Format:** JSON will be used for all request and response payloads, ensuring interoperability.
    *   **Versioning:** API versioning (e.g., `/api/v1/`) will be implemented to allow for future changes without breaking existing clients.

### 5. Authentication Approach

*   **Standard Username/Password:** As per open assumptions, standard authentication will be used.
*   **Secure Password Storage:** User passwords will be securely hashed using a strong, industry-standard algorithm (e.g., Argon2id or bcrypt) and salted before storage (NFR-S-002).
*   **Token-Based Authentication (JWT):**
    1.  Upon successful login (FR-001), the backend will issue a short-lived JSON Web Token (JWT) to the client.
    2.  This token will contain essential, non-sensitive user information, including the user's ID and assigned role(s).
    3.  The client will store this token (e.g., in `localStorage` or `httpOnly` cookies) and include it in the `Authorization` header of all subsequent API requests.
    4.  The backend will validate the JWT for authenticity and expiration on each request.
*   **Role-Based Access Control (RBAC):**
    1.  The JWT will be used to determine the authenticated user's role (Student, Teacher, Administrator).
    2.  Backend middleware/decorators will enforce access control rules (NFR-S-003), ensuring that users can only access features and data relevant to their assigned role (FR-002). For example, only teachers can create assignments, and students can only view their own grades.

### 6. Infrastructure Considerations

*   **Cloud-Native Deployment:** Leveraging a major cloud provider (e.g., AWS, GCP, Azure) is recommended for scalability, reliability, and managed services.
*   **Compute:**
    *   **Containerization (Docker):** Packaging the backend application into Docker containers for portability and consistency across environments.
    *   **Orchestration (Kubernetes/ECS/Cloud Run):** Deploying containers on a managed Kubernetes service (EKS, GKE, AKS) or Elastic Container Service (ECS) for automated scaling, healing, and deployment, addressing NFR-SC-001 and NFR-R-001.
    *   **Auto-Scaling:** Configure auto-scaling groups for backend instances to handle varying load, especially for file uploads (NFR-P-002) and concurrent users.
*   **Database:**
    *   **Managed Database Service:** Using a managed PostgreSQL service (e.g., AWS RDS for PostgreSQL, Google Cloud SQL for PostgreSQL). This provides automated backups (NFR-R-002), patching, and high availability features.
*   **File Storage:**
    *   **Object Storage Service:** AWS S3 (or equivalent) for secure and scalable file storage.
*   **Networking:**
    *   **Virtual Private Cloud (VPC):** Isolating resources in a private network.
    *   **Load Balancers:** Distributing traffic to application instances (ELB/ALB on AWS, GCLB on GCP).
    *   **HTTPS/SSL Certificates:** Enforcing HTTPS for all data in transit (NFR-S-001) via load balancers.
*   **CI/CD:** Implement Continuous Integration/Continuous Deployment pipelines to automate code quality checks, testing, and deployment, ensuring reliable and frequent updates (NFR-M-001).
*   **Monitoring & Logging:** Integrate with cloud-native monitoring (e.g., CloudWatch, Stackdriver) and centralized logging (e.g., ELK stack, Splunk) for performance tracking (NFR-P-001) and incident response.

### 7. Security Considerations

*   **Data Encryption:**
    *   **In Transit:** All communication between clients and the server, and potentially between backend services, will be encrypted using TLS/HTTPS (NFR-S-001).
    *   **At Rest:** Database data and files in object storage will be encrypted at rest using platform-managed encryption keys.
*   **Authentication & Authorization:**
    *   Robust username/password authentication with secure hashing and salting (NFR-S-002).
    *   Strict RBAC enforcement at the API level (NFR-S-003) to prevent unauthorized access.
    *   Implement rate limiting on authentication endpoints to mitigate brute-force attacks.
*   **Input Validation & Output Encoding:**
    *   Strict validation of all user inputs on the backend to prevent common vulnerabilities like SQL Injection (NFR-S-004) and XSS.
    *   Proper output encoding of all user-generated content displayed in the UI to prevent XSS attacks.
*   **File Upload Security:**
    *   Validate file types (FR-T-004) and sizes (NFR-P-002) on the backend.
    *   Store uploaded files with unique, non-executable names to prevent path traversal and arbitrary code execution.
    *   If possible, implement basic malware scanning on uploaded files (though not explicitly required, it's a strong security measure).
    *   Implement granular access control for uploaded files using pre-signed URLs or proxying through the backend.
*   **Vulnerability Management:**
    *   Regular security scanning of the codebase and dependencies.
    *   Web Application Firewall (WAF) to protect against common web exploits.
*   **Principle of Least Privilege:** Apply to all user accounts, service accounts, and infrastructure components, granting only the necessary permissions.

### 8. Scalability Considerations

*   **Stateless Backend:** The use of JWTs ensures the backend services remain stateless, allowing for easy horizontal scaling of application instances behind a load balancer.
*   **Horizontal Scaling of Compute:** The containerized application on an orchestration platform (Kubernetes/ECS) will be configured for auto-scaling based on CPU utilization, memory, or request queue depth, supporting 5,000 concurrent users (NFR-SC-001).
*   **Managed Database Scalability:** PostgreSQL on a managed service allows for vertical scaling (upgrading instance size) and implementing read replicas for read-heavy operations, offloading the primary database.
*   **Object Storage Scalability:** Amazon S3 (or equivalent) is designed for massive scalability, handling petabytes of data and billions of objects without explicit user intervention.
*   **Caching (Future Consideration):** While not critical for MVP, server-side caching (e.g., Redis) can be introduced for frequently accessed, read-heavy data (e.g., course lists) to further reduce database load and improve response times (NFR-P-001).
*   **Optimized Queries:** Database queries will be optimized with appropriate indexing to ensure efficient data retrieval under load.

### 9. Main Technical Risks

*   **Security Breaches:**
    *   **Risk:** Unauthorized access to user data or system functionalities due to flaws in authentication, authorization (RBAC), or common web vulnerabilities (NFR-S-003, NFR-S-004). File uploads could introduce malware or allow for abuse.
    *   **Mitigation:** Rigorous implementation of security best practices, including strong password hashing, thorough input validation, output encoding, granular RBAC, and regular security audits/penetration testing. Implement a WAF.
*   **Performance Bottlenecks:**
    *   **Risk:** High latency for page loads or assignment uploads, especially under heavy load (NFR-P-001, NFR-P-002). Database performance might degrade with increasing data and concurrent users.
    *   **Mitigation:** Efficient API design, optimized database queries with proper indexing, horizontal scaling of backend services, utilizing a CDN for static assets (if needed later), and leveraging cloud object storage for files. Continuous performance monitoring.
*   **Complexity of RBAC:**
    *   **Risk:** Ensuring that the granular permissions for Students, Teachers, and Administrators are correctly implemented and maintained across all features can be complex and error-prone. Incorrect implementation could lead to privilege escalation.
    *   **Mitigation:** Clear definition of roles and permissions early on, comprehensive unit and integration tests for authorization logic, and thorough manual testing across all user roles.
*   **File Upload & Management Challenges:**
    *   **Risk:** Handling large file uploads (up to 100MB) efficiently, securely, and reliably (NFR-P-002). Issues with storage cost, access control, and potential for malicious files.
    *   **Mitigation:** Direct uploads to cloud object storage (e.g., S3 pre-signed URLs), server-side validation of file types/sizes, robust error handling during uploads, and secure access patterns for downloads.
*   **Scalability Challenges (beyond MVP assumptions):**
    *   **Risk:** While the architecture aims for scalability for 5,000 concurrent users, future growth beyond this might require significant re-architecture (e.g., microservices, database sharding), leading to higher complexity and cost.
    *   **Mitigation:** Design with modularity in mind, allowing for potential decomposition into microservices. Monitor performance metrics closely to identify scaling bottlenecks early.
*   **Maintainability Debt:**
    *   **Risk:** Rapid development for MVP might lead to shortcuts in documentation, testing, and code quality, making future enhancements and bug fixes challenging (NFR-M-001).
    *   **Mitigation:** Establish and enforce coding standards, conduct regular code reviews, prioritize automated testing (unit, integration, end-to-end), and ensure adequate technical documentation from the outset.

---

## Backend Developer

As a Senior Backend Developer, my goal is to translate the provided technical architecture for EduBridge into a concrete and practical backend plan, focusing on API endpoints, data models, business logic, authentication, validations, and error handling, leveraging Python with Django REST Framework and PostgreSQL.

---

### EduBridge Backend Plan (Django REST Framework & PostgreSQL)

Based on the technical architecture, here's a detailed backend plan for the EduBridge platform, focusing on MVP features.

#### 1. API Endpoints (v1)

All API endpoints will be prefixed with `/api/v1/`.

**1.1. User & Authentication Service**
*   **`POST /api/v1/auth/register/`**: Register a new user (Student/Teacher).
    *   *Input*: `username`, `email`, `password`, `role` (default: Student).
    *   *Output*: User details (excluding password) and JWT token.
*   **`POST /api/v1/auth/login/`**: Authenticate a user.
    *   *Input*: `username` (or `email`), `password`.
    *   *Output*: User details and JWT token.
*   **`GET /api/v1/users/me/`**: Retrieve authenticated user's profile.
    *   *Auth*: JWT required.
    *   *Output*: User details.
*   **`PUT /api/v1/users/me/`**: Update authenticated user's profile.
    *   *Auth*: JWT required.
    *   *Input*: `email`, `first_name`, `last_name`, etc.
*   **`GET /api/v1/users/`**: List all users (Admin only).
    *   *Auth*: JWT, Admin role required.
    *   *Output*: List of user details.
*   **`GET /api/v1/users/{user_id}/`**: Retrieve a specific user's details (Admin only, or Teacher for their students).
    *   *Auth*: JWT, Admin/Teacher role required.
*   **`PUT /api/v1/users/{user_id}/`**: Update a specific user's details (Admin only).
    *   *Auth*: JWT, Admin role required.
*   **`DELETE /api/v1/users/{user_id}/`**: Delete a user (Admin only).
    *   *Auth*: JWT, Admin role required.

**1.2. Course & Enrollment Service**
*   **`POST /api/v1/courses/`**: Create a new course.
    *   *Auth*: JWT, Teacher role required.
    *   *Input*: `title`, `description`, `term`, `start_date`, `end_date`.
    *   *Output*: Course details.
*   **`GET /api/v1/courses/`**: List all courses (accessible to current user based on role).
    *   *Auth*: JWT required.
    *   *Output*: List of course details.
*   **`GET /api/v1/courses/{course_id}/`**: Retrieve specific course details.
    *   *Auth*: JWT required (user must be enrolled or assigned as teacher/admin).
    *   *Output*: Course details.
*   **`PUT /api/v1/courses/{course_id}/`**: Update course details.
    *   *Auth*: JWT, Teacher (assigned to course) or Admin role required.
*   **`DELETE /api/v1/courses/{course_id}/`**: Delete a course.
    *   *Auth*: JWT, Admin role required.
*   **`POST /api/v1/courses/{course_id}/enrollments/`**: Enroll student(s) in a course or assign teacher(s).
    *   *Auth*: JWT, Admin role required.
    *   *Input*: `user_ids` (list of student/teacher IDs to enroll/assign), `role` (Student/Teacher).
*   **`GET /api/v1/courses/{course_id}/enrollments/`**: List all students/teachers in a course.
    *   *Auth*: JWT, Teacher (assigned to course) or Admin role required.
*   **`DELETE /api/v1/courses/{course_id}/enrollments/{enrollment_id}/`**: Remove student/teacher from a course.
    *   *Auth*: JWT, Admin role required.

**1.3. Assignment Management Service**
*   **`POST /api/v1/courses/{course_id}/assignments/`**: Create a new assignment for a course.
    *   *Auth*: JWT, Teacher (assigned to course) or Admin role required.
    *   *Input*: `title`, `description`, `due_date`, `max_score`, `allowed_file_types` (e.g., `["pdf", "docx"]`).
    *   *Output*: Assignment details.
*   **`GET /api/v1/courses/{course_id}/assignments/`**: List assignments for a course.
    *   *Auth*: JWT required (user must be enrolled or assigned as teacher/admin).
    *   *Output*: List of assignment details.
*   **`GET /api/v1/assignments/{assignment_id}/`**: Retrieve specific assignment details.
    *   *Auth*: JWT required (user must be enrolled in course or assigned as teacher/admin).
    *   *Output*: Assignment details.
*   **`PUT /api/v1/assignments/{assignment_id}/`**: Update assignment details.
    *   *Auth*: JWT, Teacher (assigned to course) or Admin role required.
*   **`DELETE /api/v1/assignments/{assignment_id}/`**: Delete an assignment.
    *   *Auth*: JWT, Teacher (assigned to course) or Admin role required.

**1.4. Submission Service**
*   **`POST /api/v1/assignments/{assignment_id}/submissions/`**: Submit an assignment.
    *   *Auth*: JWT, Student role required.
    *   *Input*: `file` (multipart/form-data), `comments` (optional).
    *   *Output*: Submission details. This endpoint will coordinate file upload to S3 and store metadata.
*   **`GET /api/v1/assignments/{assignment_id}/submissions/me/`**: Retrieve the authenticated student's submission for an assignment.
    *   *Auth*: JWT, Student role required.
    *   *Output*: Submission details.
*   **`GET /api/v1/assignments/{assignment_id}/submissions/`**: List all submissions for an assignment.
    *   *Auth*: JWT, Teacher (assigned to course) or Admin role required.
    *   *Output*: List of submission details.
*   **`GET /api/v1/submissions/{submission_id}/`**: Retrieve details for a specific submission.
    *   *Auth*: JWT, Teacher (assigned to course) or Admin role required, or Student if it's their own submission.
    *   *Output*: Submission details.
*   **`GET /api/v1/submissions/{submission_id}/file/`**: Download submitted file.
    *   *Auth*: JWT, Teacher (assigned to course) or Admin role required, or Student if it's their own submission.
    *   *Output*: Redirect to pre-signed S3 URL or stream file directly.
    *   *Logic*: Generate a short-lived pre-signed S3 URL for download.

**1.5. Grading & Feedback Service**
*   **`POST /api/v1/submissions/{submission_id}/grade/`**: Create/Update a grade and feedback for a submission.
    *   *Auth*: JWT, Teacher (assigned to course) or Admin role required.
    *   *Input*: `score`, `feedback` (text), `is_visible` (boolean).
    *   *Output*: Grade details.
*   **`GET /api/v1/submissions/{submission_id}/grade/`**: Retrieve grade and feedback for a submission.
    *   *Auth*: JWT, Teacher (assigned to course) or Admin role required, or Student if `is_visible` is true.
    *   *Output*: Grade details.
*   **`GET /api/v1/courses/{course_id}/grades/me/`**: Retrieve authenticated student's grades for a course.
    *   *Auth*: JWT, Student role required.
    *   *Output*: List of grades for the student in that course, including overall course grade.
*   **`GET /api/v1/courses/{course_id}/grades/`**: Retrieve all grades for a course (for teachers/admins).
    *   *Auth*: JWT, Teacher (assigned to course) or Admin role required.
    *   *Output*: List of grades for all students in that course, including overall course grades.

#### 2. Data Models (PostgreSQL via Django ORM)

We'll define Django models, mapping directly to PostgreSQL tables.

*   **`User` Model (Django's `AbstractUser` or custom `User`):**
    *   `id` (PK, UUID or AutoField)
    *   `username` (CharField, unique)
    *   `email` (EmailField, unique)
    *   `password` (CharField, hashed)
    *   `first_name` (CharField)
    *   `last_name` (CharField)
    *   `role` (CharField, choices: `STUDENT`, `TEACHER`, `ADMIN`)
    *   `date_joined` (DateTimeField)
    *   `is_active` (BooleanField)
    *   `is_staff` (BooleanField, for Django Admin)

*   **`Course` Model:**
    *   `id` (PK, UUID or AutoField)
    *   `title` (CharField)
    *   `description` (TextField)
    *   `term` (CharField)
    *   `start_date` (DateField)
    *   `end_date` (DateField)
    *   `created_at` (DateTimeField)
    *   `updated_at` (DateTimeField)

*   **`Enrollment` Model (Junction table for Users and Courses):**
    *   `id` (PK, UUID or AutoField)
    *   `user` (ForeignKey to `User`)
    *   `course` (ForeignKey to `Course`)
    *   `role` (CharField, choices: `STUDENT`, `TEACHER`) - *This allows a user to be a student in one course and a teacher in another.*
    *   `enrolled_at` (DateTimeField)
    *   *Constraints*: `UniqueConstraint(fields=['user', 'course', 'role'])`

*   **`Assignment` Model:**
    *   `id` (PK, UUID or AutoField)
    *   `course` (ForeignKey to `Course`)
    *   `title` (CharField)
    *   `description` (TextField)
    *   `due_date` (DateTimeField)
    *   `max_score` (DecimalField or IntegerField)
    *   `allowed_file_types` (JSONField or ArrayField of CharField, e.g., `['pdf', 'docx']`)
    *   `created_at` (DateTimeField)
    *   `updated_at` (DateTimeField)
    *   `created_by` (ForeignKey to `User`, Teacher/Admin)

*   **`Submission` Model:**
    *   `id` (PK, UUID or AutoField)
    *   `assignment` (ForeignKey to `Assignment`)
    *   `student` (ForeignKey to `User` where `role=STUDENT`)
    *   `file_key` (CharField, S3 object key)
    *   `file_name` (CharField, original file name)
    *   `file_size` (IntegerField)
    *   `mime_type` (CharField)
    *   `comments` (TextField, optional)
    *   `submitted_at` (DateTimeField)
    *   `is_resubmission` (BooleanField, default False)
    *   *Constraints*: `UniqueConstraint(fields=['assignment', 'student'], name='unique_submission_per_assignment')` for initial submission. Subsequent submissions would either update this or create new records marked as `is_resubmission=True` with a versioning strategy. For MVP, we might simply update the existing submission record for resubmissions.

*   **`Grade` Model:**
    *   `id` (PK, UUID or AutoField)
    *   `submission` (OneToOneField to `Submission`)
    *   `grader` (ForeignKey to `User` where `role=TEACHER` or `ADMIN`)
    *   `score` (DecimalField, e.g., 5,2 for 100.00)
    *   `feedback` (TextField, optional)
    *   `is_visible` (BooleanField, default False)
    *   `graded_at` (DateTimeField)

#### 3. Business Logic

The backend will implement the following core logic:

*   **User Management:**
    *   **Registration (`POST /auth/register`):** Hash passwords using `bcrypt` or `Argon2id` (Django's default) and salt before saving. Assign default `STUDENT` role.
    *   **Login (`POST /auth/login`):** Verify password against hash. If successful, generate and return a JWT containing `user_id`, `username`, and `role`.
    *   **Profile Management:** Allow users to update their own non-sensitive profile information. Admin users can manage all users.
*   **Course Management:**
    *   **Creation/Update:** Enforce Teacher/Admin role. Associate `created_by` field.
    *   **Retrieval:** Filter courses based on the authenticated user's enrollment (for Students) or teaching assignments (for Teachers). Admins can see all.
*   **Enrollment:**
    *   **Enrollment/Assignment:** Only Admin can enroll students or assign teachers to courses. Validate that `user_ids` correspond to existing users and roles are valid.
*   **Assignment Management:**
    *   **Creation/Update:** Enforce Teacher/Admin role. Associate `created_by` and `course`.
    *   **Validation:** Ensure `due_date` is in the future, `max_score` is positive, and `allowed_file_types` is a list of valid extensions.
*   **Submission Handling:**
    *   **File Upload (`POST /assignments/{assignment_id}/submissions`):**
        1.  Validate user is a student enrolled in the course, and the assignment is not past its `due_date` (for initial submission).
        2.  Validate file type against `assignment.allowed_file_types` and size against NFR-P-002 (e.g., 100MB max).
        3.  Generate a unique `file_key` (e.g., UUID-based) for S3 storage.
        4.  Use Django's file upload handling to process the incoming file.
        5.  Initiate a direct upload to Amazon S3. The backend will likely *not* proxy the file but rather provide a pre-signed URL to the frontend for direct upload, or handle the upload itself if using smaller files and initial simpler architecture. For large files, direct client-to-S3 with a pre-signed URL is preferred.
        6.  Store `file_key`, `file_name`, `file_size`, `mime_type` and other metadata in the `Submission` model.
    *   **Resubmission:** If `due_date` allows, update the existing `Submission` record with the new `file_key` and other details. Potentially mark the previous file_key as 'archived' in S3 or use versioning.
    *   **File Download (`GET /submissions/{submission_id}/file`):**
        1.  Authorize access: Only the student who submitted it, the teacher of the course, or an admin can download.
        2.  Generate a short-lived (e.g., 1-hour expiration) pre-signed S3 URL for the `file_key`.
        3.  Redirect the client to this pre-signed URL or proxy the download through the backend (less scalable).
*   **Grading & Feedback:**
    *   **Create/Update Grade:** Enforce Teacher/Admin role. Associate `grader` and `submission`. Validate `score` is within `0` and `assignment.max_score`.
    *   **Overall Course Grade Calculation:** Based on `Assignment.max_score` and `Grade.score` for each assignment, calculate a weighted average (if weights are introduced later) or simple average for the student in the course. This can be a computed property or a background task.
    *   **Visibility:** Respect `is_visible` flag for students.

#### 4. Authentication

*   **Django REST Framework JWT:** Use `djangorestframework-simplejwt` or a similar library.
*   **Login Flow:**
    1.  User sends `username`/`email` and `password` to `POST /api/v1/auth/login/`.
    2.  Backend authenticates using `User.check_password()`.
    3.  If successful, a JWT (access token) and optionally a refresh token are generated.
    4.  Access token contains `user_id`, `username`, `role`.
    5.  Client stores token (e.g., in `localStorage`) and sends it in `Authorization: Bearer <token>` header for subsequent requests.
*   **Authorization (RBAC):**
    1.  **Middleware/Decorators:** Django REST Framework permissions classes will enforce `IsAuthenticated` and custom `IsAdminUser`, `IsTeacher`, `IsStudent`, or `IsCourseOwnerOrAdmin` rules.
    2.  **Role Check:** The `role` claim in the JWT will be used to determine the user's permissions.
    3.  **Object-Level Permissions:** For resources like courses, assignments, and submissions, ensure the authenticated user has the right to view/modify (e.g., a teacher can only grade submissions for their assigned courses). This will be handled within DRF's `Permission` classes or view logic.
*   **Password Storage:** Django's default password hasher (e.g., PBKDF2 with SHA256, or configurable to Argon2id/bcrypt) will be used for secure password storage with salting.

#### 5. Validations

Input validation will be strictly enforced at the API level using Django REST Framework serializers and model validators.

*   **User Inputs:**
    *   **Required Fields:** Ensure all mandatory fields are present.
    *   **Data Types:** Validate fields match expected types (e.g., email format for `email`, date format for `due_date`).
    *   **Length Constraints:** Apply max/min length for text fields (`title`, `description`).
    *   **Uniqueness:** Enforce unique `username` and `email` for users.
    *   **Password Complexity:** Implement policies for minimum length, character types (if needed beyond Django's default).
*   **Business Logic Validations:**
    *   **Roles:** Check if the authenticated user has the necessary `role` for the action (e.g., only Teachers can create assignments).
    *   **Dates:** `start_date` before `end_date`, `due_date` in the future for new assignments/submissions.
    *   **Scores:** Grades must be within `0` and `max_score` for an assignment.
    *   **File Uploads:**
        *   **File Type:** Validate uploaded file's MIME type and extension against `allowed_file_types`.
        *   **File Size:** Enforce max file size (100MB).
        *   **Malicious Content:** Basic checks (e.g., prevent executable file extensions, though full malware scanning is a later enhancement).
*   **Database Constraints:** Utilize PostgreSQL's foreign key constraints and unique constraints (e.g., `user`-`course` unique combination in `Enrollment`) to maintain data integrity.

#### 6. Error Handling

A consistent error response structure will be used for all API endpoints, typically returning JSON.

*   **HTTP Status Codes:**
    *   `200 OK`: Successful GET, PUT, PATCH, DELETE.
    *   `201 Created`: Successful POST.
    *   `204 No Content`: Successful DELETE with no content to return.
    *   `400 Bad Request`: Validation errors, malformed requests.
    *   `401 Unauthorized`: Missing or invalid authentication token.
    *   `403 Forbidden`: Authenticated user does not have permission for the action/resource (RBAC failure).
    *   `404 Not Found`: Resource not found.
    *   `405 Method Not Allowed`: HTTP method not supported for the endpoint.
    *   `409 Conflict`: Resource conflict (e.g., trying to create a user with an existing email).
    *   `500 Internal Server Error`: Unexpected server-side errors.
    *   `503 Service Unavailable`: Temporary server unavailability (e.g., database connection issues).
*   **JSON Error Format:**
    ```json
    {
        "status": "error",
        "code": 400,
        "message": "Invalid input provided.",
        "details": {
            "field_name": ["Error message for field 1.", "Another error message."],
            "non_field_errors": ["General error message."]
        }
    }
    ```
*   **Specific Error Types:**
    *   **Authentication Errors:** Invalid credentials, token expired, token missing.
    *   **Authorization Errors:** Insufficient permissions (e.g., student trying to create a course).
    *   **Validation Errors:** Detailed messages per field from DRF serializers.
    *   **Resource Not Found:** When accessing `/api/v1/courses/{course_id}/` with a non-existent `course_id`.
    *   **File Upload Errors:** Invalid file type, file too large, S3 upload failure.
*   **Logging:** All server-side errors (especially 5xx) will be logged with sufficient detail for debugging (stack traces, request context).
*   **Rate Limiting:** Implement rate limiting on authentication endpoints to prevent brute-force attacks. Django REST Framework provides tools for this.

This plan provides a solid foundation for the backend development of EduBridge, adhering to the architectural guidelines and focusing on the core backend responsibilities.

---

## Frontend Developer

As the Senior Frontend Developer, my goal is to translate the EduBridge Backend Plan into a concrete frontend implementation plan, focusing on user-facing elements, interactions, and overall experience. This plan will leverage modern web technologies to create a dynamic and responsive application.

---

### EduBridge Frontend Implementation Plan

Based on the detailed backend plan, here’s a frontend implementation strategy focusing on screens, user flows, components, state management, forms, validations, navigation, and user experience.

#### I. Core Technologies & Architecture

*   **Framework:** React (or a similar component-based library like Vue/Angular) for building the user interface.
*   **Routing:** React Router DOM (for React) for declarative navigation.
*   **State Management:**
    *   **Server State (Data Fetching):** React Query (or SWR) for managing data fetching, caching, synchronization, and error handling with the backend APIs. This will significantly simplify data management.
    *   **Client State (UI State):** Zustand (or Redux Toolkit for larger, more complex global states) for managing local UI state (e.g., form inputs, modal visibility, auth status).
*   **Styling:** Tailwind CSS (or Material-UI, Chakra UI) for utility-first styling and rapid UI development.
*   **Forms:** React Hook Form (or Formik) for robust form management, validation, and submission.
*   **Authentication:** JWT stored securely (e.g., HTTP-only cookies if using a proxy, or `localStorage`/`sessionStorage` with careful security considerations for SPA). Interceptors for automatically attaching tokens to API requests.
*   **Build Tool:** Vite or Next.js (if server-side rendering/static site generation is desired for performance/SEO, otherwise a client-side React app is sufficient for MVP).

#### II. Global Frontend Elements & Considerations

1.  **Authentication & Authorization:**
    *   **JWT Handling:** Store the JWT token securely after login. Include it in the `Authorization` header for all protected API calls.
    *   **Role-Based UI:** Dynamically render navigation items, buttons, and content blocks based on the user's `role` (Student, Teacher, Admin) obtained from the JWT.
    *   **Protected Routes:** Implement client-side route guards to prevent unauthorized access to specific pages.
2.  **Global State:**
    *   **Auth Context/Store:** Maintain user authentication status (`isAuthenticated`), user details (`user_id`, `username`, `role`), and the JWT token.
    *   **Loading/Error Indicators:** Implement global loading spinners/skeletons and toast notifications for API call statuses.
3.  **Responsive Design:** Ensure all screens and components adapt gracefully to various screen sizes (mobile, tablet, desktop).
4.  **Error Handling & Notifications:**
    *   Display user-friendly error messages from backend API responses (e.g., 400 Bad Request details in forms, 401/403 for access issues, 404 for not found).
    *   Use a toast notification system (e.g., `react-toastify`) for success messages, warnings, and non-blocking errors.
5.  **Accessibility (A111y):** Follow WCAG guidelines for semantic HTML, keyboard navigation, and ARIA attributes where appropriate.

#### III. Core UI Components

*   **Auth Components:**
    *   `LoginForm`: `username`/`email`, `password` inputs.
    *   `RegisterForm`: `username`, `email`, `password`, `confirm_password`, `role` (dropdown, default Student).
*   **Navigation:**
    *   `Header`: Logo, user avatar/name, logout button.
    *   `Sidebar/Main Navigation`: Role-based links (e.g., "My Courses", "All Courses", "Users (Admin)", "Create Course (Teacher/Admin)").
*   **User Profile:**
    *   `UserProfileDisplay`: Shows user details (`first_name`, `last_name`, `email`, `role`).
    *   `UserProfileEditForm`: Inputs for editable fields.
*   **Data Display:**
    *   `TableComponent`: Generic component for displaying lists (Users, Courses, Assignments, Submissions, Grades).
    *   `CardComponent`: For displaying individual course/assignment summaries.
*   **Forms:**
    *   `ControlledInput`: Reusable input component with validation feedback.
    *   `TextArea`: For descriptions, feedback.
    *   `DatePicker`: For `start_date`, `end_date`, `due_date`.
    *   `FileUploadInput`: Specifically for assignment submissions.
    *   `SelectInput`: For `role` selection in register/enrollment, `allowed_file_types`.
*   **Modals & Dialogs:** For confirmations (e.g., delete actions), detailed views.
*   **Loading/Empty/Error States:** Placeholder components or UI elements for different data states.

#### IV. User Flows & Screens (Role-Based)

This section maps backend endpoints to frontend screens and user interactions.

**A. Authentication & User Management**

1.  **Public Screens:**
    *   **`/login` (Login Screen):**
        *   **Form:** `LoginForm`
        *   **Flow:** Submit credentials to `POST /api/v1/auth/login/`. On success, store JWT, update auth state, redirect to `/courses`. On error, display messages (e.g., "Invalid credentials").
        *   **Navigation:** Link to `/register`.
    *   **`/register` (Registration Screen):**
        *   **Form:** `RegisterForm`
        *   **Flow:** Submit data to `POST /api/v1/auth/register/`. On success, show success message, redirect to `/login`. On error, display validation errors.

2.  **Authenticated User Screens:**
    *   **`/profile` (My Profile Screen):**
        *   **Data Fetching:** `GET /api/v1/users/me/`.
        *   **Components:** `UserProfileDisplay`, `UserProfileEditForm`.
        *   **Flow:** User can click "Edit Profile" to toggle between display and edit mode. Submit updates to `PUT /api/v1/users/me/`.
    *   **`/admin/users` (Admin: User List Screen):**
        *   **Data Fetching:** `GET /api/v1/users/` (Admin only).
        *   **Components:** `TableComponent` displaying users (`username`, `email`, `role`, actions).
        *   **Actions:** View user details, Edit, Delete.
    *   **`/admin/users/:user_id` (Admin: User Detail Screen):**
        *   **Data Fetching:** `GET /api/v1/users/{user_id}/`.
        *   **Components:** `UserProfileDisplay`, `UserProfileEditForm`.
        *   **Actions:** `PUT /api/v1/users/{user_id}/` (edit), `DELETE /api/v1/users/{user_id}/` (delete, with confirmation).

**B. Course Management**

1.  **`/courses` (Course List Screen):**
    *   **Data Fetching:** `GET /api/v1/courses/` (filtered by user role/enrollment).
    *   **Components:** `TableComponent` or `CardComponent` grid for courses (`title`, `description`, `term`, `dates`).
    *   **Actions:**
        *   **Teacher/Admin:** "Create New Course" button (links to `/courses/new`).
        *   All roles: Click on a course to navigate to `/courses/:course_id`.
    *   **UX:** Search and filter options (by term, title).
2.  **`/courses/new` (Teacher/Admin: Create Course Screen):**
    *   **Form:** `CourseForm` (`title`, `description`, `term`, `start_date`, `end_date`).
    *   **Flow:** Submit to `POST /api/v1/courses/`. On success, redirect to new course's detail page.
3.  **`/courses/:course_id` (Course Detail Screen):**
    *   **Data Fetching:** `GET /api/v1/courses/{course_id}/`.
    *   **Components:**
        *   Course overview (`title`, `description`, `term`, dates).
        *   Section for `AssignmentList` (links to `/courses/:course_id/assignments`).
        *   **Teacher/Admin Only:** Section for `EnrollmentList` (users enrolled in this course), `EnrollmentForm` (to add/remove students/teachers).
    *   **Actions:**
        *   **Teacher (assigned) / Admin:** "Edit Course" (`/courses/:course_id/edit`), "Delete Course" (with confirmation), "Add Assignment" (`/courses/:course_id/assignments/new`).
        *   **Admin:** Manage Enrollments (`POST /api/v1/courses/{course_id}/enrollments/`, `DELETE /api/v1/courses/{course_id}/enrollments/{enrollment_id}/`).
4.  **`/courses/:course_id/edit` (Teacher/Admin: Edit Course Screen):**
    *   **Data Fetching:** Pre-fill `CourseForm` with data from `GET /api/v1/courses/{course_id}/`.
    *   **Flow:** Submit updates to `PUT /api/v1/courses/{course_id}/`.

**C. Assignment Management**

1.  **`/courses/:course_id/assignments` (Assignment List for Course):**
    *   *(Often integrated into Course Detail Screen)*
    *   **Data Fetching:** `GET /api/v1/courses/{course_id}/assignments/`.
    *   **Components:** `TableComponent` or `CardComponent` for assignments (`title`, `due_date`, `max_score`).
    *   **Actions:**
        *   All roles: Click to navigate to `/assignments/:assignment_id`.
        *   **Teacher (assigned) / Admin:** "Create New Assignment" button (`/courses/:course_id/assignments/new`).
2.  **`/courses/:course_id/assignments/new` (Teacher/Admin: Create Assignment Screen):**
    *   **Form:** `AssignmentForm` (`title`, `description`, `due_date`, `max_score`, `allowed_file_types` (multi-select/tags input)).
    *   **Flow:** Submit to `POST /api/v1/courses/{course_id}/assignments/`.
3.  **`/assignments/:assignment_id` (Assignment Detail Screen):**
    *   **Data Fetching:** `GET /api/v1/assignments/{assignment_id}/`.
    *   **Components:**
        *   Assignment overview (`title`, `description`, `due_date`, `max_score`, `allowed_file_types`).
        *   **Student Only:** `SubmissionStatus` (submitted/not submitted), `SubmissionForm` (`FileUploadInput`, `comments`), "View My Submission" link.
        *   **Teacher/Admin Only:** `SubmissionList` (table of all student submissions for this assignment).
    *   **Actions:**
        *   **Teacher (assigned) / Admin:** "Edit Assignment" (`/assignments/:assignment_id/edit`), "Delete Assignment" (with confirmation).
4.  **`/assignments/:assignment_id/edit` (Teacher/Admin: Edit Assignment Screen):**
    *   **Data Fetching:** Pre-fill `AssignmentForm` with `GET /api/v1/assignments/{assignment_id}/`.
    *   **Flow:** Submit updates to `PUT /api/v1/assignments/{assignment_id}/`.

**D. Submission Service**

1.  **Student Flow (within Assignment Detail):**
    *   **`SubmissionForm`:**
        *   **Components:** `FileUploadInput` (accepts specified `allowed_file_types`), `TextArea` for `comments`.
        *   **Flow:** Submit form data (multipart/form-data) to `POST /api/v1/assignments/{assignment_id}/submissions/`.
        *   **UX:** File selection, progress bar for upload, validation of file type/size (client-side before upload), confirmation after successful upload. Handle resubmissions by allowing re-upload before `due_date`.
    *   **`MySubmissionDetails`:**
        *   **Data Fetching:** `GET /api/v1/assignments/{assignment_id}/submissions/me/`.
        *   **Components:** Displays submitted `file_name`, `comments`, `submitted_at`. "Download My File" button (`GET /api/v1/submissions/{submission_id}/file/`).
2.  **Teacher/Admin Flow (within Assignment Detail):**
    *   **`SubmissionList`:**
        *   **Data Fetching:** `GET /api/v1/assignments/{assignment_id}/submissions/`.
        *   **Components:** `TableComponent` showing student name, `file_name`, `submitted_at`, current grade status, actions.
        *   **Actions:** "View Submission" (links to `/submissions/:submission_id`), "Download File" (`GET /api/v1/submissions/{submission_id}/file/`), "Grade Submission" (links to `/submissions/:submission_id/grade`).

**E. Grading & Feedback Service**

1.  **`/submissions/:submission_id` (Submission Detail Screen):**
    *   **Data Fetching:** `GET /api/v1/submissions/{submission_id}/`.
    *   **Components:** Displays submission details, `DownloadFileButton`.
    *   **Teacher/Admin Only:**
        *   `GradeForm`: (`score`, `feedback`, `is_visible` checkbox).
        *   **Flow:** Submit to `POST /api/v1/submissions/{submission_id}/grade/` (or PUT if updating).
    *   **Student Only:**
        *   `GradeDisplay`: Displays `score`, `feedback` (if `is_visible` is true).
2.  **`/courses/:course_id/grades/me` (Student: My Grades for Course Screen):**
    *   **Data Fetching:** `GET /api/v1/courses/{course_id}/grades/me/`.
    *   **Components:** `TableComponent` listing assignments, student's score, max score, and overall course grade.
3.  **`/courses/:course_id/grades` (Teacher/Admin: Course Gradebook Screen):**
    *   **Data Fetching:** `GET /api/v1/courses/{course_id}/grades/`.
    *   **Components:** `TableComponent` showing all students, their grades for each assignment, and calculated overall course grades.
    *   **Actions:** Links to individual submission/grade for editing.

#### V. Forms & Validations

*   **Client-Side Validation:** Implement schema-based validation (e.g., Yup, Zod with React Hook Form) to provide immediate feedback to users for:
    *   Required fields
    *   Email format
    *   Password complexity (min length, special chars)
    *   Date ranges (`start_date < end_date`, `due_date` in future)
    *   Numeric ranges (`score` within `0` and `max_score`)
    *   File type and size limits (before upload to S3).
*   **Server-Side Validation Display:** Clearly map and display error messages returned from the backend (400 Bad Request details) next to the relevant form fields.

#### VI. User Experience (UX) Enhancements

*   **Optimistic UI Updates:** For non-critical actions (e.g., marking an item as read), update UI immediately and revert if API fails.
*   **Skeleton Loaders:** Display loading skeletons while data is being fetched to improve perceived performance.
*   **Form Persistence:** Consider saving draft forms locally (e.g., via `localStorage`) for long forms.
*   **Clear Call-to-Actions:** Use descriptive button labels.
*   **Visual Feedback:** Highlight successfully submitted forms, provide clear error states.
*   **Confirmation Dialogs:** For destructive actions (e.g., deleting a course, assignment, or user).
*   **Drag-and-Drop File Upload:** Enhance the file submission experience.
*   **Rich Text Editor:** For `description` fields (courses, assignments) and `feedback` fields (grades) to allow formatting.

This plan provides a robust framework for frontend development, ensuring a clear mapping to the backend services while prioritizing an intuitive and efficient user experience across different user roles.

---

## Qa Tester

As a Senior QA Tester, I've reviewed the EduBridge Frontend Implementation Plan. It provides a solid foundation with clear technology choices and a good mapping of user flows. My focus is to highlight potential quality issues, testing gaps, and risks to ensure a robust and user-friendly application.

Here are my observations, organized by the plan's sections:

---

### QA Review: EduBridge Frontend Implementation Plan

#### I. Core Technologies & Architecture

*   **General:** The chosen technologies are modern and well-supported, which bodes well for maintainability and development efficiency.
*   **Authentication (JWT Storage):**
    *   **Issue/Risk:** Storing JWTs in `localStorage` or `sessionStorage` introduces significant Cross-Site Scripting (XSS) vulnerability. An attacker exploiting XSS could easily steal the token. HTTP-only cookies are generally safer for this reason. If `localStorage`/`sessionStorage` is chosen, the plan needs to explicitly mention robust XSS protection measures (e.g., Content Security Policy, meticulous input sanitization).
    *   **Test Case:** Verify XSS protection mechanisms by attempting to inject scripts that try to read `localStorage`/`sessionStorage` and send data.
*   **State Management (React Query / SWR):**
    *   **Test Case:** Verify behavior when data becomes stale (e.g., an admin deletes a user, but another admin's list of users doesn't update until re-fetch). Ensure caching strategies are appropriate for the application's data volatility.
    *   **Edge Case:** How does the UI handle prolonged network unavailability or partial data fetching failures for a component?

#### II. Global Frontend Elements & Considerations

1.  **Authentication & Authorization:**
    *   **Role-Based UI:**
        *   **Test Case:** Thoroughly test all permutations of roles (Student, Teacher, Admin) for every UI element mentioned (navigation, buttons, content blocks). Ensure no unauthorized elements are rendered or accessible.
        *   **Edge Case:** What happens if a user's role changes mid-session (e.g., Admin demotes a Teacher)? Does the UI update dynamically or require re-login?
        *   **Integration Risk:** Discrepancy between client-side role display and actual backend authorization. Ensure backend consistently validates all actions, irrespective of frontend UI.
    *   **Protected Routes:**
        *   **Issue:** Client-side route guards alone are insufficient for security. While they prevent UI navigation, an attacker could still directly access a protected URL if the backend isn't equally robust.
        *   **Test Case:** Attempt to directly navigate to protected routes (e.g., `/admin/users`) without being logged in or with an incorrect role, bypassing the UI navigation. Ensure a proper 401/403 response and user-friendly redirect.
    *   **JWT Handling:**
        *   **Test Case:** Simulate token expiration (client-side and server-side). Verify auto-logout, session refresh (if applicable), and clear user notification.
        *   **Missing:** "Forgot Password" and "Reset Password" flows are critical authentication components not detailed in the public screens.
        *   **Usability:** How is the user informed about an expired session? Is it a silent redirect or a modal/toast?
2.  **Global State (Auth Context/Store):**
    *   **Test Case:** Verify that `isAuthenticated`, `user_id`, `username`, and `role` are consistently updated across the application post-login, logout, and profile updates.
3.  **Responsive Design:**
    *   **Test Case:** Beyond standard device sizes, test across various browser window sizes, orientations (portrait/landscape), and text zoom levels to ensure UI integrity and usability.
    *   **Usability:** Ensure touch targets are appropriately sized for mobile devices.
4.  **Error Handling & Notifications:**
    *   **Validation Gap:** How are generic 500-level server errors handled? Are they logged for developers and presented as a "Something went wrong" message to the user, or do they expose technical details?
    *   **Test Case:** Simulate various API error codes (400, 401, 403, 404, 429 Rate Limit, 500, 503) and verify user-friendly messages are displayed, and critical operations aren't left in an undefined state.
    *   **Usability:** Ensure toast notifications are not intrusive, disappear gracefully, and are accessible for screen readers. What happens if multiple toasts appear simultaneously?
5.  **Accessibility (A111y):**
    *   **Test Case:** Comprehensive keyboard navigation testing for all interactive elements (forms, buttons, links, modals, tables, date pickers).
    *   **Test Case:** Use a screen reader (e.g., NVDA, VoiceOver) to navigate through critical user flows and forms. Ensure all content is readable and interactive elements are correctly announced.
    *   **Missing:** Color contrast checks for all UI elements, especially text and interactive components, to meet WCAG AA or AAA standards.

#### III. Core UI Components

*   **`RegisterForm`:**
    *   **Edge Case:** If the `role` dropdown defaults to 'Student', how can an Admin or Teacher account be created? This implies an admin-only registration pathway or a different registration form for privileged users.
    *   **Validation Gap:** Password complexity rules should be clearly defined and validated both client-side and server-side.
*   **`TableComponent`:**
    *   **Missing:** Pagination, sorting, and filtering are crucial for tables displaying many items (Users, Courses, Assignments, Submissions). This should be explicitly part of the component's functionality.
    *   **Test Case:** Test tables with zero results, one result, and a very large number of results (requiring pagination).
    *   **Usability:** Ensure column headers are clear and sortable indicators are present.
*   **`DatePicker`:**
    *   **Edge Case:** Timezone handling. If a due date is set for "midnight" in one timezone, how does it appear or behave for a user in another timezone?
    *   **Test Case:** Verify date selections, date range constraints (e.g., start date before end date).
*   **`FileUploadInput`:**
    *   **Test Case:** Test with various file types (allowed and disallowed), file sizes (min, max, zero-byte), and special characters in file names.
    *   **Integration Risk:** Ensure the client-side validation for file types/sizes correctly aligns with backend (S3/API) limits.
    *   **Usability:** Clear feedback for file selection, upload progress, and upload failures.
*   **`Modals & Dialogs`:**
    *   **Test Case:** Verify focus trapping within the modal, proper closing with Esc key or outside click, and correct focus restoration after closing.
    *   **Accessibility:** Ensure aria attributes are correctly used.

#### IV. User Flows & Screens (Role-Based)

**A. Authentication & User Management**

*   **`/login` & `/register`:**
    *   **Test Case:** Test input sanitization for all text fields to prevent XSS.
    *   **Test Case:** Test "Remember Me" functionality (if implemented), ensuring session persistence and token security.
    *   **Edge Case:** What if the user is already logged in and tries to access `/login` or `/register`? Should redirect to a dashboard.
*   **`/admin/users` & `/admin/users/:user_id`:**
    *   **Test Case:** Verify robust authorization; non-admin users should receive a 403 Forbidden on the backend if attempting to access these routes or API endpoints.
    *   **Edge Case:** Deleting a user who is currently logged in, or who has significant associated data (courses, submissions). Confirm backend cascade behavior and UI refresh for other admins.

**B. Course Management**

*   **`/courses` (Course List Screen):**
    *   **Missing:** Search and filter options are mentioned but not detailed. These need specific test cases for various criteria, empty results, and edge cases (e.g., searching for special characters).
    *   **Test Case:** Verify role-based visibility of "Create New Course" button.
*   **`/courses/:course_id` (Course Detail Screen):**
    *   **Integration Risk:** If a course is deleted, ensure all associated assignments and enrollments are also handled correctly (backend cascade/soft delete) and the frontend gracefully handles the deleted resource.
    *   **Test Case (EnrollmentForm):** Adding a non-existent user, adding an already enrolled user.

**C. Assignment Management**

*   **`/courses/:course_id/assignments/new`:**
    *   **Validation Gap:** `due_date` validation should prevent setting a date in the past.
    *   **Test Case:** Inputting `max_score` outside the expected range (e.g., negative, excessively high).
*   **`/assignments/:assignment_id` (Assignment Detail Screen):**
    *   **Test Case (Student SubmissionForm):**
        *   Attempt to submit after the `due_date`.
        *   Network interruptions during upload.
        *   Re-submitting a file before the `due_date` (should overwrite previous, or create a new version depending on backend logic).
        *   Submit a file that fails client-side validation (type, size).
        *   Submit a file that passes client-side but fails server-side validation.
    *   **Usability:** Provide clear feedback if resubmission is not allowed or if the deadline has passed.

**D. Submission Service**

*   **Student Flow:**
    *   **Test Case (FileUploadInput UX):** Verify the progress bar accuracy and graceful handling of upload cancellations or errors.
    *   **Edge Case:** What if the file upload completes but the API call to record the submission fails?
*   **Teacher/Admin Flow:**
    *   **Test Case:** Verify the "Download File" functionality, especially for large files or files with unusual characters in their names.

**E. Grading & Feedback Service**

*   **`/submissions/:submission_id`:**
    *   **Test Case (Teacher/Admin GradeForm):**
        *   Inputting `score` values outside `0` and `max_score`.
        *   Submitting with empty `feedback`.
        *   Toggle `is_visible` and verify student view updates correctly.
*   **`/courses/:course_id/grades` (Teacher/Admin: Course Gradebook Screen):**
    *   **Performance:** For courses with many students and assignments, test the performance of this screen (data fetching, rendering).
    *   **Missing:** Common features for gradebooks include export (CSV/Excel) functionality. This might be a future enhancement, but worth noting.

#### V. Forms & Validations

*   **Client-Side Validation:**
    *   **Test Case:** Test all specific validation rules (`required`, `email`, password complexity, `start_date < end_date`, `due_date` in future, numeric ranges, file type/size).
    *   **Usability:** Ensure validation messages are clear, concise, and appear near the relevant input field.
    *   **Edge Case:** What happens if the validation library (Yup/Zod) schema doesn't perfectly match the backend validation rules? Ensure server errors are consistently displayed.
*   **Server-Side Validation Display:**
    *   **Test Case:** Verify that detailed error messages from the backend (e.g., "Email already exists") are correctly parsed and displayed in the corresponding form fields, rather than as a generic error toast.

#### VI. User Experience (UX) Enhancements

*   **Optimistic UI Updates:**
    *   **Test Case:** Critically test the rollback mechanism. Simulate API failure immediately after an optimistic update. Ensure the UI reverts correctly and provides appropriate error feedback.
*   **Skeleton Loaders:**
    *   **Test Case:** Verify loaders appear correctly for all data fetching, and disappear once data is loaded (or an error is shown). Ensure they don't flash if data loads very quickly.
*   **Form Persistence:**
    *   **Test Case:** Test saving drafts, navigating away, and returning. How is the draft cleared (e.g., after successful submission, or if the user explicitly cancels)?
*   **Confirmation Dialogs:**
    *   **Test Case:** Ensure all destructive actions (delete course, assignment, user) trigger a confirmation dialog. Verify "Cancel" and "Confirm" paths work correctly.
*   **Drag-and-Drop File Upload:**
    *   **Test Case:** Test with various browsers, operating systems, and file types. Test dragging multiple files (if supported).
*   **Rich Text Editor:**
    *   **Test Case:** Test all formatting options. Input very long text, special characters, and attempt XSS injections to ensure sanitization is robust before saving to the backend.

---

This detailed review should help in refining the frontend implementation plan and preparing for comprehensive testing throughout the development lifecycle. My primary concern remains robust security for authentication and consistent, helpful feedback for all user interactions.

---

## Tech Lead

## Technical Review and Recommendation: EduBridge Platform

**Review Date:** October 26, 2023

**Project:** EduBridge - MVP Release

### 1. Overall Assessment

The EduBridge team has put together a comprehensive set of documents covering requirements, architecture, and initial backend and frontend implementation plans, complemented by a thorough QA review. The chosen tech stack (React, Django REST Framework, PostgreSQL, AWS S3) is robust and suitable for a scalable web application. The logical breakdown of services and the focus on MVP features are well-aligned with the product vision.

However, a detailed review reveals several critical inconsistencies, risks, and missing elements that require immediate attention to ensure a secure, functional, and user-friendly MVP.

### 2. Analysis of Each Section

#### 2.1. Requirements (PRD)

*   **Strengths:** Clear product vision, well-defined target users, concise MVP features, and detailed functional requirements. Non-functional requirements (NFRs) cover crucial aspects like performance, security, usability, reliability, scalability, and maintainability. Open assumptions clearly define the MVP boundaries.
*   **Inconsistencies/Gaps:**
    *   **Forgot Password/Reset Password:** This fundamental authentication feature is not explicitly listed in FR-001 (Secure login/logout) or any other section, nor is it accounted for in the authentication assumptions. This is a critical omission for any production system.
    *   **Teacher Account Creation:** FR-A-001 states "Administrators shall be able to create new user accounts... specifying... user role." This implies administrators are the sole creators of Teacher accounts. However, the Backend and Frontend plans implicitly suggest self-registration for teachers. This needs clarification and alignment.
    *   **Grade Calculation Detail:** FR-S-006 and FR-T-009 mention overall course grades. The "Grade Calculation" assumption clarifies "Basic grade calculation (e.g., sum, average) is assumed for overall course grades. Complex grading schemes, weighting, or rubrics are out of scope for MVP." This is good, but the Backend Plan mentions "weighted average (if weights are introduced later) or simple average." For MVP, it should definitively be "simple average" to align with the assumption.

#### 2.2. Architecture

*   **Strengths:** Excellent choice of modern and scalable technologies. Logical separation into services, even if deployed as a modular monolith for MVP, is a sound strategy for future growth. Comprehensive coverage of security, scalability, infrastructure, and explicit identification of technical risks. The use of AWS S3 for file storage with pre-signed URLs is appropriate for performance and security.
*   **Inconsistencies/Gaps:**
    *   **JWT Storage Details:** The architecture mentions JWT for authentication but does not explicitly define *how* it will be securely stored on the client-side. This leaves a gap that the QA findings correctly highlight as a significant security vulnerability (XSS).
    *   **Timezone Handling:** Not explicitly detailed in the architecture, but critical for an educational platform dealing with deadlines (`due_date`, `start_date`, `end_date`) across potentially different user timezones. This is a common source of bugs and user frustration.
    *   **Automated Testing Strategy:** While NFR-M-001 (Maintainability) implies good code quality and standards, the architecture could benefit from explicitly outlining an automated testing strategy (unit, integration, E2E) for both backend and frontend.

#### 2.3. Backend Plan

*   **Strengths:** Detailed API endpoint definitions that map well to functional requirements. Robust data models with appropriate relationships and constraints. Business logic clearly outlines authentication, role enforcement, and file handling using S3. Strong emphasis on input validation and a consistent error handling strategy.
*   **Inconsistencies/Gaps:**
    *   **Teacher Registration:** As noted in the PRD, the `POST /api/v1/auth/register/` endpoint allowing a `role` input for `Student/Teacher` contradicts the PRD's assertion that Administrators create user accounts. This requires alignment.
    *   **Resubmission Strategy:** The plan states, "For MVP, we might simply update the existing submission record for resubmissions." This is a concrete decision, which is good. However, it means previous versions of a submission are lost, which might not be ideal long-term. For MVP, this might be acceptable but worth noting the implication.
    *   **Timezone Implementation:** No explicit mention of storing dates in UTC and handling timezone conversions for `due_date`, `start_date`, `end_date`.

#### 2.4. Frontend Plan

*   **Strengths:** Excellent choice of React ecosystem tools for a modern SPA. Well-structured global elements, UI components, and detailed user flows mapped directly to backend endpoints. Client-side validation using schema-based libraries is a good practice, and planning for server-side error display is crucial for UX. UX enhancements are well thought out.
*   **Inconsistencies/Gaps:**
    *   **JWT Storage:** States `localStorage` or `sessionStorage` *with careful security considerations* or `httpOnly` cookies. This is not a definitive secure strategy and aligns with QA's critical finding regarding XSS vulnerability.
    *   **Forgot/Reset Password:** No screens or flows for this essential feature.
    *   **Teacher Registration UI:** The `RegisterForm` explicitly includes a `role` dropdown defaulting to `Student`, allowing for teacher self-registration. This requires alignment with the PRD.
    *   **Table Functionality:** Mentions `TableComponent` but lists pagination, sorting, and filtering as a UX enhancement rather than a core component requirement for usability (NFR-U-001) for potentially large datasets (e.g., `/admin/users`, `/courses/:course_id/grades`). This should be integral.
    *   **Rich Text Editor (RTE):** Mentioned under UX enhancements for `description` and `feedback`. While improving UX, RTEs introduce significant security complexity (XSS) and are often deferred for MVP. If included, robust sanitization *must* be a core functional requirement, not just a UX enhancement.

#### 2.5. QA Findings

*   **Strengths:** The QA review is exceptionally thorough, identifying critical security vulnerabilities, functional gaps, edge cases, and usability improvements across the entire frontend plan. It provides concrete test cases and highlights crucial integration risks.
*   **Critical Findings:**
    *   **JWT Storage (XSS):** Confirms `localStorage`/`sessionStorage` as a major vulnerability.
    *   **Missing "Forgot Password" / "Reset Password":** Validates this as a key functional omission.
    *   **Role-Based Access Control (RBAC):** Emphasizes backend enforcement and edge cases like role changes mid-session.
    *   **Timezone Handling:** Highlights this as a critical edge case for `DatePicker`.
    *   **Table Features:** Reinforces the need for pagination, sorting, and filtering.
    *   **RTE Security:** Points out the XSS risk associated with rich text editors.
    *   **500-level error handling, Accessibility, Optimistic UI rollback:** Excellent attention to detail on NFRs and advanced UX.

### 3. Key Risks Identified

1.  **Security Risk (High - Critical):** The proposed JWT storage mechanism (`localStorage`/`sessionStorage`) in the frontend plan presents a significant XSS vulnerability. This is a critical security flaw that must be addressed definitively. The lack of a "Forgot/Reset Password" flow further compounds authentication security risks.
2.  **Functional Gap (High):** The complete absence of a "Forgot Password" and "Reset Password" flow is a major functional and security deficiency for an MVP. Users will inevitably forget passwords, and without this, the system is not truly usable for the target audience.
3.  **Inconsistent Requirements (Medium):** The ambiguity around Teacher self-registration versus Admin-only creation needs resolution to align PRD with implementation plans.
4.  **Usability & Maintainability Risk (Medium):** Lack of detailed planning for pagination, sorting, and filtering in data tables will quickly degrade usability for NFR-U-001 as data grows. Unaddressed timezone issues will lead to incorrect deadlines and user frustration.
5.  **Maintainability Debt (Medium):** While NFR-M-001 is mentioned, explicit automated testing strategies (unit, integration, E2E) are not detailed across the plans. Without this, technical debt can accumulate rapidly, especially with rapid MVP development.
6.  **XSS Risk with Rich Text Editor (Medium if implemented):** If a Rich Text Editor is introduced for MVP, the security implications regarding XSS must be thoroughly addressed on both client and server.

### 4. Technical Recommendation

Based on the detailed review, I recommend the following actions:

1.  **Mandatory Security Enhancements (Immediate Action):**
    *   **JWT Storage:** Abandon `localStorage`/`sessionStorage` for JWT access tokens. Implement **HTTP-only cookies** for both access tokens (short-lived) and refresh tokens (longer-lived) to mitigate XSS vulnerabilities. The backend should handle token issuance, refreshing, and cookie management.
    *   **Forgot/Reset Password Flow:** **Immediately incorporate** "Forgot Password" and "Reset Password" functionality into the PRD (as an extension of FR-001), Backend Plan (new API endpoints, logic for token generation/validation, email sending capability), and Frontend Plan (new screens and user flows). This is non-negotiable for a secure and functional MVP.
    *   **RTE Security:** If a Rich Text Editor is implemented for MVP, a **robust sanitization library** (e.g., DOMPurify on frontend, Python's `bleach` on backend) must be integrated and explicitly tested to prevent XSS attacks (NFR-S-004). If this cannot be guaranteed, defer RTE to a later release and use plain text.

2.  **Requirements & Scope Clarification:**
    *   **Teacher Registration:** Clarify the PRD's stance on Teacher account creation. If self-registration for teachers is desired, update FR-A-001 to reflect this, and ensure the backend and frontend plans are aligned. If admin-only, restrict the `role` dropdown in the frontend `RegisterForm` and remove `role` from the backend `auth/register` endpoint (Admin would use the `/users` endpoints to create teachers).
    *   **Grade Calculation:** Confirm that for MVP, overall course grades will be a **simple average** of assignment scores, aligning precisely with the "Grade Calculation" assumption.

3.  **Critical Usability & Reliability Features:**
    *   **Table Functionality:** **Integrate pagination, sorting, and basic filtering** as core features for all `TableComponent` usages (Users, Courses, Assignments, Submissions, Grades) in the Frontend Plan. This is essential for meeting NFR-U-001 and handling growing data volumes.
    *   **Timezone Handling:** Implement a comprehensive timezone strategy. The **backend must store all date/time information in UTC**. Frontend should fetch UTC times and convert them to the user's local timezone for display, clearly indicating the timezone when appropriate (e.g., due dates). This is critical for academic deadlines.

4.  **Development Process & Quality Assurance:**
    *   **Automated Testing:** Augment both Backend and Frontend plans with an explicit **automated testing strategy**, including tools/frameworks (e.g., Pytest for Django, Jest/React Testing Library for React) and targets for unit, integration, and end-to-end test coverage to ensure NFR-M-001 and overall quality.
    *   **API Documentation:** Begin developing and maintaining **API documentation** (e.g., using OpenAPI/Swagger tools with Django REST Framework) from the outset to facilitate frontend-backend collaboration and future onboarding/maintenance.
    *   **Error Handling Details:** Ensure detailed error messages (especially 5xx) are logged server-side for debugging but are presented as **user-friendly, non-technical messages** to the user on the frontend.
    *   **QA Collaboration:** Maintain close collaboration with QA throughout the development lifecycle, especially for security, authentication, authorization, and critical user flows, leveraging the detailed test cases provided.

By addressing these recommendations, EduBridge can proceed with a more robust, secure, and user-friendly MVP, setting a solid foundation for future development.

---

