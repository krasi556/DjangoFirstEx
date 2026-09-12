import datetime
from django.core.management.base import BaseCommand
from qualifications.models import Qualifications
from people.models import People
from address.models import Address


class Command(BaseCommand):
    help = "Populate the database with rich, realistic, real-looking mock data."

    def add_arguments(self, parser):
        parser.add_argument(
            '--clear',
            action='store_true',
            help='Clear all existing data in Qualifications, People, and Address before seeding.',
        )

    def handle(self, *args, **options):
        if options['clear']:
            self.stdout.write(self.style.WARNING("Clearing existing database records..."))
            address_count, _ = Address.objects.all().delete()
            people_count, _ = People.objects.all().delete()
            qualifications_count, _ = Qualifications.objects.all().delete()
            self.stdout.write(
                self.style.SUCCESS(
                    f"Cleared: {address_count} Addresses, {people_count} People, {qualifications_count} Qualifications."
                )
            )

        # Let's check if data already exists to avoid duplication if --clear was not run
        if People.objects.exists() or Qualifications.objects.exists() or Address.objects.exists():
            self.stdout.write(
                self.style.WARNING(
                    "Database is not empty. Running without --clear might cause duplicate records."
                )
            )

        self.stdout.write("Starting to seed database with realistic records...")

        # We will define our realistic, correlated profiles.
        profiles_data = [
            {
                "name": "Dr. Evelyn Martinez",
                "age": 42,
                "job_description": "Lead Cardiologist",
                "qualifications": [
                    {
                        "university": "Johns Hopkins University",
                        "courses": "Doctor of Medicine (M.D.)",
                        "date": datetime.date(2010, 5, 20)
                    },
                    {
                        "university": "Harvard University",
                        "courses": "Cardiovascular Fellowship",
                        "date": datetime.date(2013, 6, 15)
                    }
                ],
                "addresses": [
                    {
                        "street": "721 Broadway Street, Apt 4B",
                        "city": "Baltimore",
                        "country": "United States"
                    }
                ]
            },
            {
                "name": "Aiko Tanaka",
                "age": 29,
                "job_description": "Senior UX/UI Designer",
                "qualifications": [
                    {
                        "university": "Kyoto University",
                        "courses": "B.A. in Product Design",
                        "date": datetime.date(2019, 3, 25)
                    }
                ],
                "addresses": [
                    {
                        "street": "3-chome-15-1 Minami-Aoyama",
                        "city": "Minato-ku, Tokyo",
                        "country": "Japan"
                    }
                ]
            },
            {
                "name": "Marcus Vance",
                "age": 35,
                "job_description": "Director of AI Research",
                "qualifications": [
                    {
                        "university": "Stanford University",
                        "courses": "Ph.D. in Computer Science (AI/ML Focus)",
                        "date": datetime.date(2016, 12, 10)
                    },
                    {
                        "university": "MIT",
                        "courses": "M.S. in Electrical Engineering",
                        "date": datetime.date(2012, 6, 5)
                    }
                ],
                "addresses": [
                    {
                        "street": "844 Palo Alto Avenue",
                        "city": "Palo Alto",
                        "country": "United States"
                    },
                    {
                        "street": "55 Main Street, Suite 201",
                        "city": "Cambridge",
                        "country": "United States"
                    }
                ]
            },
            {
                "name": "Liam O'Connor",
                "age": 27,
                "job_description": "Environmental Scientist",
                "qualifications": [
                    {
                        "university": "University of Oxford",
                        "courses": "B.Sc. in Earth Sciences",
                        "date": datetime.date(2021, 7, 12)
                    }
                ],
                "addresses": [
                    {
                        "street": "12 High Street",
                        "city": "Oxford",
                        "country": "United Kingdom"
                    }
                ]
            },
            {
                "name": "Sarah Jenkins",
                "age": 31,
                "job_description": "Investment Portfolio Manager",
                "qualifications": [
                    {
                        "university": "London School of Economics",
                        "courses": "M.Sc. in Finance & Economics",
                        "date": datetime.date(2017, 9, 30)
                    }
                ],
                "addresses": [
                    {
                        "street": "88 Canary Wharf Blvd",
                        "city": "London",
                        "country": "United Kingdom"
                    }
                ]
            },
            {
                "name": "Hans Müller",
                "age": 48,
                "job_description": "Senior Automotive Systems Architect",
                "qualifications": [
                    {
                        "university": "Technical University of Munich",
                        "courses": "M.Sc. in Automotive Software Engineering",
                        "date": datetime.date(2003, 11, 22)
                    }
                ],
                "addresses": [
                    {
                        "street": "Schwanthalerstraße 14",
                        "city": "Munich",
                        "country": "Germany"
                    }
                ]
            },
            {
                "name": "Chloe Dupont",
                "age": 24,
                "job_description": "Junior Frontend Engineer",
                "qualifications": [
                    {
                        "university": "Sorbonne University",
                        "courses": "B.Sc. in Computer Science",
                        "date": datetime.date(2024, 6, 20)
                    }
                ],
                "addresses": [
                    {
                        "street": "45 Rue de la Harpe",
                        "city": "Paris",
                        "country": "France"
                    }
                ]
            },
            {
                "name": "David Kovac",
                "age": 38,
                "job_description": "Chief Operations Officer",
                "qualifications": [
                    {
                        "university": "INSEAD",
                        "courses": "Executive MBA",
                        "date": datetime.date(2018, 12, 15)
                    },
                    {
                        "university": "Charles University",
                        "courses": "B.Sc. in Economics",
                        "date": datetime.date(2010, 6, 18)
                    }
                ],
                "addresses": [
                    {
                        "street": "Celetná 20",
                        "city": "Prague",
                        "country": "Czech Republic"
                    }
                ]
            },
            {
                "name": "Dr. Sophia Rodriguez",
                "age": 33,
                "job_description": "Quantum Physicist",
                "qualifications": [
                    {
                        "university": "ETH Zurich",
                        "courses": "Ph.D. in Quantum Computing",
                        "date": datetime.date(2018, 5, 14)
                    }
                ],
                "addresses": [
                    {
                        "street": "Rämistrasse 101",
                        "city": "Zurich",
                        "country": "Switzerland"
                    }
                ]
            },
            {
                "name": "James Chen",
                "age": 21,
                "job_description": "Undergraduate Software Intern",
                "qualifications": [
                    {
                        "university": "University of Waterloo",
                        "courses": "Software Engineering Co-op",
                        "date": datetime.date(2025, 4, 30)
                    }
                ],
                "addresses": [
                    {
                        "street": "200 University Ave W",
                        "city": "Waterloo",
                        "country": "Canada"
                    }
                ]
            }
        ]

        created_people_count = 0
        created_qual_count = 0
        created_address_count = 0

        # Create records
        for profile in profiles_data:
            # Create or get the qualifications first
            qual_objs = []
            for qual in profile["qualifications"]:
                # Use get_or_create to prevent duplication if same qualification exists
                qual_obj, created = Qualifications.objects.get_or_create(
                    university=qual["university"],
                    courses=qual["courses"],
                    date=qual["date"]
                )
                if created:
                    created_qual_count += 1
                qual_objs.append(qual_obj)

            # Create the person (use update_or_create or get_or_create based on name)
            person_obj, created_person = People.objects.get_or_create(
                name=profile["name"],
                defaults={
                    "age": profile["age"],
                    "job_description": profile["job_description"]
                }
            )

            # If person wasn't created (existed), we update their age and job description to match
            if not created_person:
                person_obj.age = profile["age"]
                person_obj.job_description = profile["job_description"]
                person_obj.save()
            else:
                created_people_count += 1

            # Associate qualifications with person
            person_obj.qualifications.set(qual_objs)

            # Create addresses for the person
            for addr in profile["addresses"]:
                # Use get_or_create to avoid duplicate addresses
                addr_obj, created_addr = Address.objects.get_or_create(
                    person=person_obj,
                    street=addr["street"],
                    city=addr["city"],
                    country=addr["country"]
                )
                if created_addr:
                    created_address_count += 1

            self.stdout.write(f"Successfully processed profile: {profile['name']}")

        self.stdout.write(
            self.style.SUCCESS(
                f"\nDatabase population completed successfully!\n"
                f"Created / Verified:\n"
                f" - {created_people_count} People\n"
                f" - {created_qual_count} New Qualifications\n"
                f" - {created_address_count} New Addresses"
            )
        )
