# FinPilot

FinPilot is a personal financial-health and planning web application designed to help users understand their money situation in a simple, transparent way.

## What the project will do

The application is planned to help users:
- track income, expenses, loans, savings, and financial goals
- calculate cash flow and key financial ratios
- assess emergency-fund coverage
- review debt health
- calculate an explainable financial-health score
- identify financial priorities and surplus allocation choices
- view historical financial progress
- review market context separately from personal finances

The project is intentionally focused on clear, understandable financial planning rather than opaque automated recommendations.

## Planned architecture

The initial structure is organized into a few clear areas:
- `engine/`: financial calculations and analysis logic
- `database/`: data access and persistence helpers for personal finance records
- `auth/`: future authentication support
- `market/`: future market-data access and context display
- `ui/`: Streamlit pages and user-facing screens
- `tests/`: placeholder and future validation tests

## Folder responsibilities

### `engine/`
Contains future financial logic for cash flow, debt, emergency planning, goals, health scoring, priorities, and allocation decisions.

### `database/`
Will eventually hold database access helpers and data models for income, expenses, loans, goals, and historical records.

### `auth/`
Will eventually include authentication and user-session logic.

### `market/`
Will eventually provide any market-related context or data retrieval.

### `ui/`
Will hold the Streamlit pages for the dashboard, analysis, income, expenses, loans, goals, market information, and history.

### `tests/`
Will contain unit tests and project validation checks as the application grows.

## Current status

This repository currently contains the initial project skeleton only.

The code in this project is intentionally simple, beginner-friendly, and does not yet implement:
- financial calculations
- Supabase connectivity
- authentication flow
- market API integration
- fake or hard-coded user data

The goal of this stage is to establish the project layout and basic structure for future development.
