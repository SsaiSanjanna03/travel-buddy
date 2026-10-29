# Vyoma LLC: Week 1 Technical Work Log

## Project Information

- **Project:** Travel Discovery Application
- **Company:** Vyoma LLC
- **Name:** Ssai Sanjanna Ganji
- **Role:** Founder and Software Engineer
- **Reporting period:** October 16, 2026 - October 22 2026
- **Total hours worked:** 24
- **Work location:** Principle office (Home)

## Weekly Objective

Establish the initial product requirements and technical design for a location-based travel discovery application that helps users explore local food, coffee, and drink recommendations.

## Daily Activity Log

### Day 1: Project Overview and Repository Setup

- **Date:** October 16, 2026
- **Hours worked:** 3 hours
- **Activities performed:**
  - Defined or refined the initial product concept and intended users.
  - Created or updated `README.md` with the project overview, proposed technology stack, MVP direction, repository structure, and roadmap.
- **Deliverables:** `README.md`
- **Evidence or references:** Git code

### Day 2: Software Requirements Analysis

- **Date:** October 17, 2026
- **Hours worked:** 5 hours
- **Activities performed:**
  - Identified the problem the application is intended to address.
  - Documented target users, functional requirements, non-functional requirements, constraints, acceptance criteria, and open questions.
- **Deliverables:** `docs/requirements.md`
- **Evidence or references:** Git code

### Day 3: User Stories and MVP Scope

- **Date:** October 19, 2026
- **Hours worked:** 6 hours
- **Activities performed:**
  - Defined user stories and acceptance criteria for place discovery, category filtering, nearby search, and place details.
  - Documented the proposed minimum viable product (MVP), exclusions, and initial success criteria.
- **Deliverables:** `docs/user-stories.md`, `docs/mvp-scope.md`
- **Evidence or references:** Git code

### Day 4: Architecture and Data Model

- **Date:** October 20, 2026
- **Hours worked:** 6 hours
- **Activities performed:**
  - Outlined the proposed application components and request flow.
  - Drafted the planned API endpoints, including `GET /health` and `GET /places`.
  - Defined the proposed place data model, fields, validation considerations, and geographic-search approach.
- **Deliverables:** `docs/architecture.md`, `docs/data-model.md`
- **Evidence or references:** Git code

### Day 5: Data-Source Evaluation and Weekly Review

- **Date:** October 22, 2026
- **Hours worked:** 5 hours
- **Activities performed:**
  - Documented criteria for evaluating potential place-data sources, including commercial-use permissions, attribution, storage and caching rules, rate limits, and costs.
  - Recorded unresolved data-source questions and next steps.
  - Reviewed the week's documentation and identified priorities for the next development period.
- **Deliverables:** `docs/data-source-evaluation.md`, `docs/work-log.md`, and this weekly review
- **Evidence or references:** Git code

## Deliverables Summary

| File                             | Purpose                                                      | Status    |
| -------------------------------- | ------------------------------------------------------------ | --------- |
| `README.md`                      | Project overview, proposed stack, MVP direction, and roadmap | Completed |
| `docs/requirements.md`           | Functional and non-functional requirements                   | Completed |
| `docs/user-stories.md`           | User stories and acceptance criteria                         | Completed |
| `docs/mvp-scope.md`              | MVP scope, exclusions, and success criteria                  | Completed |
| `docs/architecture.md`           | Proposed components, request flow, and API design            | Completed |
| `docs/data-model.md`             | Proposed place entity and data relationships                 | Completed |
| `docs/data-source-evaluation.md` | Criteria for evaluating potential data sources               | Completed |
| `docs/work-log.md`               | Reusable daily and weekly work-log template                  | Completed |
| `docs/week-1-review.md`          | Weekly activity summary                                      | Completed |

## Technical Decisions and Open Questions

- **Initial backend direction:** Python with FastAPI and Pydantic is proposed for the API.
- **Initial testing direction:** Pytest is proposed for automated tests.
- **Initial data approach:** Use sample or manually curated data for the first prototype while evaluating potential data sources and their applicable terms.
- **Data-source compliance:** Confirm permissions, attribution requirements, storage and caching restrictions, rate limits, and costs before integrating an external source.

## Next Week's Objective

Subject to the actual project plan, the next development period may focus on:

- Establishing the development environment.
- Implementing a basic health endpoint.
- Defining the place data model.
- Building an initial place-search API.
- Adding input validation and automated tests.

## Weekly Review

- **Work completed:** Established the initial project documentation and technical design for Vyoma LLC's location-based travel discovery application. Documented the project overview, functional and non-functional requirements, user stories, MVP scope, proposed system architecture, data model, and criteria for evaluating potential data sources. Identified initial technical decisions, open questions, and priorities for the next development phase.
- **Total hours worked this week:** 25 hours
- **Note:** Will push code at the end of week 1 or week 2 for now
