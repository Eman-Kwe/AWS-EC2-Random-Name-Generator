# EC2-Random-Name-Generator

A Python-based tool for generating standardized EC2 instance names with department-based authorization controls.

## Overview

This project provides an automated solution for generating EC2 instance names following organizational naming conventions. By restricting name generation to authorized departments only, it ensures governance, security, and cost management across AWS resources.

## Benefits

### Standardization and Governance

* Enforces consistent naming conventions across the organization
* Prevents inconsistent or random naming schemes that complicate resource management
* Helps enforce tagging policies and cost allocation standards

### Security and Compliance

* Implements department-based access control for resource naming
* Prevents shadow IT scenarios where unauthorized teams create resources
* Creates an audit trail linking resources to requesting departments
* Supports compliance requirements for resource tracking and accountability

### Automation and Efficiency

* Automates the naming process to reduce manual errors
* Speeds up deployment workflows
* Integrates with CI/CD pipelines and Infrastructure as Code tools
* Eliminates dependency on outdated documentation

### Cost Management

* Enables department-based spending tracking through standardized naming patterns
* Simplifies identification of resource consumption by business unit
* Facilitates accurate cost allocation and chargeback processes

## Features

* **Department Authorization:** Only authorized departments (Marketing, Accounting, FinOps) can generate EC2 names
* **Batch Generation:** Create multiple instance names in a single operation
* **Naming Convention Enforcement:** Automatically applies organizational standards
* **Case-Insensitive Validation:** Accepts department input in any case (e.g., "marketing", "MARKETING", "Marketing")

## Naming Format

Each generated name follows this pattern:

```
<Department>-<6 random uppercase letters><4 random digits>
```

Example output:

```
Marketing-JKVBRL4821
Accounting-WNXTQF7390
Finops-AMHPDS6154
```

## Requirements

* Python 3.x
* No external dependencies — uses only Python's built-in `random` and `string` modules

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/<your-username>/EC2-Random-Name-Generator.git
   cd EC2-Random-Name-Generator
   ```

2. No additional packages required.

## Usage

Run the script:

```bash
python ec2_name_generator.py
```

### Authorized Department Example

```
How many EC2 instances do you want to name?
3
Enter your department: Marketing
Marketing-JKVBRL4821
Marketing-WNXTQF7390
Marketing-AMHPDS6154
```

### Unauthorized Department Example

```
How many EC2 instances do you want to name?
2
Enter your department: HR
This department is not authorized to use EC2 Name Generator.
```

## Authorized Departments

| Department | Status     |
|------------|------------|
| Marketing  | Authorized |
| Accounting | Authorized |
| FinOps     | Authorized |
| All Others | Denied     |
