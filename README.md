# nycdb

Let's research the landlord! New York City is in a housing crisis. Some [landlords](https://youtu.be/o1SzKHXz8tU) leave their buildings in despair and let their tenants suffer without heat in winter. Others evict their tenants, legally or illegally, in order to flip buildings and profit off of gentrification. Affordable housing is a scarce resource.

Residents, lawyers, tenants, and organizers who want to use data in their struggle turn to proprietary databases and resources, like PropertyShark, designed for real estate or contend with CSV and printouts from city websites. _nycdb_ aims to give technologists and researchers who want to volunteer their time helping community groups who are defending the city against the real estate industry a leg up by providing a ready-to-use database filled with housing data.

**nycdb** is a python program that downloads, processes, and loads the following public datasets into postgres:

- Department of City Planning's Pluto: versions 15v1, 16v2, 17v1, 18v1, 18v2, and 19v1
- DOB Job Filings
- [DOB Complaints](https://github.com/nycdb/nycdb/wiki/Dataset:-DOB-Complaints)
- [DOB Violations](https://github.com/nycdb/nycdb/wiki/Dataset:-DOB-Violations)
- [HPD Violations](https://github.com/nycdb/nycdb/wiki/Dataset:-HPD-Violations)
- HPD Registrations
- [HPD Complaints](https://github.com/nycdb/nycdb/wiki/Dataset:-HPD-Complaints)
- [HPD Repair and Vacate Orders](https://github.com/nycdb/nycdb/wiki/Dataset:-HPD-Vacate-Orders)
- Department of Finance Rolling Sales
- Tax bills - Rent Stabilization Unit Counts (John Krauss's data)
- [ACRIS](https://github.com/nycdb/nycdb/wiki/Dataset:-ACRIS)
- 2017 Marshal Evictions
- [ECB Violations](https://github.com/nycdb/nycdb/wiki/Dataset:-ECB-Violations)
- [Oath Hearings](https://github.com/nycdb/nycdb/wiki/Dataset:-OATH-Hearings)
- Property Address Directory
- J-51 Exemptions

## Using the database

### Download a copy

If you just want a copy of the postgres database, you may download the latest versions:

- [nyc-db-2019-11-15.sql.bz2](https://nycdb.info/sql/nyc-db-2019-11-15.sql.bz2)
- [nyc-db-2019-07-24.sql.bz2](https://nycdb.info/sql/nyc-db-2019-07-24.sql.bz2)

[![License: CC BY-NC-SA 4.0](https://licensebuttons.net/l/by-nc-sa/4.0/80x15.png)](https://creativecommons.org/licenses/by-nc-sa/4.0/)

[See here](https://github.com/nycdb/nycdb/wiki/Loading-a-copy-into-postgres) for instructions on how to load the database file.

### Use the Housing Data Coalition's instance

The Housing Data Coalition hosts their own copy ("instance") of nycdb. If you are not a member of HDC and would like to use it, please contact housingdatacoalition@gmail.com

## Using the software

Go to [src/README.md](src/README.md) for documentation on creating your own copy of the database. See the folder [/ansible](/ansible) for ansible playbooks that can be used to install a copy of the database on a sever.

### Acknowledgments

- [Heatseek](https://heatseek.org/) for ongoing support of the project and for their amazing work.
- [@talos](https://github.com/talos) for his [tax bill scrapping](https://github.com/talos/nyc-stabilization-unit-counts) to get counts of rent-stabilization units
- NYCDB's [programmers](https://github.com/nycdb/nycdb/graphs/contributors)
- [Housing Data Coalition](https://www.housingdatanyc.org/) for their support and for hosting nycdb workshops

#### License: AGPLv3

```
NYCDB - Postgres database of NYC housing data
Copyright (C) 2016-2019 ziggy & contributors

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
GNU Affero General Public License for more details.
```

The database files provided on this page are licensed [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/legalcode).
