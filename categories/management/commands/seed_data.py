from django.core.management.base import BaseCommand
from categories.models import Category
from notes.models import Note


class Command(BaseCommand):
    help = 'Seeds the database with meaningful and real-world categories and notes.'

    def handle(self, *args, **options):
        self.stdout.write(self.style.WARNING("Clearing existing Categories and Notes from the database..."))
        
        # Clear existing data
        notes_deleted, _ = Note.objects.all().delete()
        categories_deleted, _ = Category.objects.all().delete()
        
        self.stdout.write(self.style.SUCCESS(
            f"Successfully cleared {notes_deleted} notes and {categories_deleted} categories."
        ))
        
        self.stdout.write(self.style.MIGRATE_HEADING("\nSeeding new Categories and Notes..."))

        # Define data structure
        seed_data = [
            {
                "category_title": "Programming & Software Development",
                "category_body": "Notes, tips, and best practices about web development, programming languages, clean code standards, and modern development workflows.",
                "notes": [
                    {
                        "title": "Mastering Python List Comprehensions",
                        "body": (
                            "List comprehensions provide a concise way to create lists in Python. "
                            "They are often more efficient and readable than traditional for loops.\n\n"
                            "### Syntax\n"
                            "`[expression for item in iterable if condition]`\n\n"
                            "### Examples\n"
                            "1. **Basic conversion:**\n"
                            "   ```python\n"
                            "   squares = [x**2 for x in range(10)]\n"
                            "   ```\n"
                            "2. **With filtering (if):**\n"
                            "   ```python\n"
                            "   even_squares = [x**2 for x in range(10) if x % 2 == 0]\n"
                            "   ```\n"
                            "3. **With conditional expression (if-else):**\n"
                            "   ```python\n"
                            "   results = [x if x > 5 else 0 for x in range(10)]\n"
                            "   ```\n\n"
                            "### Best Practices\n"
                            "- **Keep them simple:** If a list comprehension is longer than one or two lines, split it into a traditional loop or a helper function.\n"
                            "- **Avoid nesting:** Avoid nested list comprehensions when readability is compromised."
                        ),
                        "is_published": True
                    },
                    {
                        "title": "RESTful API Design Best Practices",
                        "body": (
                            "Building robust, clean, and maintainable REST APIs is essential for modern web application architectures.\n\n"
                            "### Key Principles\n"
                            "1. **Use HTTP Verbs Explicitly:**\n"
                            "   - `GET`: Retrieve a resource.\n"
                            "   - `POST`: Create a new resource.\n"
                            "   - `PUT`/`PATCH`: Update an existing resource.\n"
                            "   - `DELETE`: Remove a resource.\n"
                            "2. **Use Nouns, Not Verbs in URIs:**\n"
                            "   - Good: `GET /api/v1/notes`\n"
                            "   - Bad: `GET /api/v1/get_all_notes`\n"
                            "3. **Use Plural Nouns:**\n"
                            "   - Use `/categories` rather than `/category`.\n"
                            "4. **Provide Proper HTTP Status Codes:**\n"
                            "   - `200 OK`: Successful request.\n"
                            "   - `201 Created`: Successful creation of a resource.\n"
                            "   - `400 Bad Request`: Validation or request payload error.\n"
                            "   - `401 Unauthorized`: Authentication missing or failed.\n"
                            "   - `403 Forbidden`: Authenticated, but lacks permissions.\n"
                            "   - `404 Not Found`: Resource does not exist.\n"
                            "   - `500 Internal Server Error`: Server-side crash or unhandled error."
                        ),
                        "is_published": True
                    },
                    {
                        "title": "The Importance of Git Commit Messages",
                        "body": (
                            "Writing descriptive commit messages helps teams understand *why* changes were made and makes the git history a valuable diagnostic tool.\n\n"
                            "### The Imperative Mood\n"
                            "Always write commit messages in the imperative mood, as if commanding the codebase:\n"
                            "- **Good:** `Add authentication middleware for endpoints`\n"
                            "- **Bad:** `Added authentication middleware` or `Adds authentication middleware`\n\n"
                            "### Structure of a Great Commit Message\n"
                            "```\n"
                            "Summarize changes in 50 characters or less\n\n"
                            "More detailed explanatory text, if necessary. Wrap it to\n"
                            "about 72 characters. The blank line separating the summary\n"
                            "from the body is critical.\n"
                            "```"
                        ),
                        "is_published": True
                    }
                ]
            },
            {
                "category_title": "Productivity & Habit Building",
                "category_body": "Systems, methodologies, and habits that help optimize daily focus, energy, and workflow organization.",
                "notes": [
                    {
                        "title": "The Pomodoro Technique Explained",
                        "body": (
                            "The Pomodoro Technique is a time management method developed by Francesco Cirillo in the late 1980s. "
                            "It uses a timer to break work down into intervals, traditionally 25 minutes in length, separated by short breaks.\n\n"
                            "### How it Works\n"
                            "1. **Choose a task** you want to accomplish.\n"
                            "2. **Set a timer** for 25 minutes (one Pomodoro).\n"
                            "3. **Work on the task** with absolute focus until the timer rings.\n"
                            "4. **Take a short break** (5 minutes). This represents a transition and allows mental recovery.\n"
                            "5. **Repeat** the cycle. After every 4 Pomodoros, take a longer break (15-30 minutes).\n\n"
                            "### Key Benefits\n"
                            "- Enhances concentration by eliminating interruptions.\n"
                            "- Reduces cognitive fatigue through scheduled rest.\n"
                            "- Helps measure and track effort spent on various tasks."
                        ),
                        "is_published": True
                    },
                    {
                        "title": "Building Atomic Habits",
                        "body": (
                            "Habits are the compound interest of self-improvement. Small 1% improvements every day accumulate into massive changes over time.\n\n"
                            "### The Four Laws of Behavior Change\n"
                            "To build a good habit, follow these four simple principles:\n"
                            "1. **Make it Obvious:** Design your environment so cues for good habits are visible.\n"
                            "2. **Make it Attractive:** Pair a habit you *need* to do with a habit you *want* to do.\n"
                            "3. **Make it Easy:** Reduce friction. Start with habits that take less than two minutes (The Two-Minute Rule).\n"
                            "4. **Make it Satisfying:** Use immediate rewards to reinforce the habit."
                        ),
                        "is_published": True
                    },
                    {
                        "title": "Getting Things Done (GTD) Framework",
                        "body": (
                            "GTD is a popular productivity framework created by David Allen based on a simple premise: your brain is for having ideas, not holding them.\n\n"
                            "### Five Steps of GTD\n"
                            "1. **Capture:** Collect everything that has your attention into an 'inbox'.\n"
                            "2. **Clarify:** Decide if each item is actionable. If yes, what is the next step?\n"
                            "3. **Organize:** File actionable items under projects, context, or calendar.\n"
                            "4. **Reflect:** Review your lists regularly (weekly) to keep the system clean and up to date.\n"
                            "5. **Engage:** Simply execute the next action based on your current energy, priority, and time."
                        ),
                        "is_published": True
                    }
                ]
            },
            {
                "category_title": "Personal Finance & Investing",
                "category_body": "Practical principles for budgeting, managing debt, emergency funding, and long-term asset building.",
                "notes": [
                    {
                        "title": "Understanding the 50/30/20 Budgeting Rule",
                        "body": (
                            "A straightforward guideline to distribute after-tax income to manage daily spending and build wealth.\n\n"
                            "### Allocation Percentages\n"
                            "- **50% Needs:** Essential living expenses (housing, utilities, groceries, healthcare, minimum loan repayments).\n"
                            "- **30% Wants:** Discretionary spending (dining out, entertainment, travel, hobbies, subscriptions).\n"
                            "- **20% Savings & Debt:** Financial goals (emergency fund contributions, retirement accounts, extra principal payments on high-interest debt).\n\n"
                            "### Why it Works\n"
                            "It provides a simple high-level view of finances without requiring the granular tracking of every single cent."
                        ),
                        "is_published": True
                    },
                    {
                        "title": "Emergency Fund Essentials",
                        "body": (
                            "An emergency fund is a stash of cash set aside to cover unexpected financial surprises, such as medical bills, car repairs, or job loss.\n\n"
                            "### Key Guidelines\n"
                            "1. **How much to save:** Aim for 3 to 6 months' worth of living expenses.\n"
                            "2. **Where to keep it:** In a high-yield savings account (HYSA) that is liquid and easily accessible, but separate from your primary checking account.\n"
                            "3. **When to use it:** Only for genuine emergencies that are urgent, unexpected, and necessary."
                        ),
                        "is_published": True
                    },
                    {
                        "title": "The Power of Compound Interest",
                        "body": (
                            "Compound interest is interest calculated on the initial principal, which also includes all of the accumulated interest of previous periods.\n\n"
                            "### Key Formula\n"
                            "`A = P * (1 + r/n)**(nt)`\n\n"
                            "### Takeaways\n"
                            "- **Time is your greatest ally:** The earlier you start investing, the more time your interest has to compound.\n"
                            "- **Consistency matters:** Regular, systematic contributions outperform trying to time the market.\n"
                            "- **Reinvest dividends:** Ensure any distributions are automatically reinvested to maximize the compounding effect."
                        ),
                        "is_published": True
                    }
                ]
            },
            {
                "category_title": "Culinary Arts & Cooking",
                "category_body": "Techniques, fundamental skills, and classic recipes for home cooks and kitchen enthusiasts.",
                "notes": [
                    {
                        "title": "Knife Safety and Essential Cuts",
                        "body": (
                            "Knife skills are the absolute foundation of efficient and safe cooking. Mastering them speeds up prep time and ensures uniform cooking.\n\n"
                            "### Core Rules of Knife Safety\n"
                            "1. **Keep knives sharp:** Dull knives are more likely to slip and cause injury.\n"
                            "2. **The 'Claw' Grip:** Curl the fingers of your non-dominant hand inward to hold the food, guiding the flat of the knife blade with your knuckles.\n"
                            "3. **Never catch a falling knife:** Step back and let it fall.\n\n"
                            "### Common Cuts\n"
                            "- **Julienne:** Matchstick-sized strips (approx. 1/8 x 1/8 x 2 inches).\n"
                            "- **Dice (Small, Medium, Large):** Cubing food into uniform squares.\n"
                            "- **Chiffonade:** Rolling leafy greens (like basil) and slicing them into thin ribbons."
                        ),
                        "is_published": True
                    },
                    {
                        "title": "Perfect Roasted Chicken Recipe",
                        "body": (
                            "A classic culinary benchmark that highlights the importance of temperature control and simple seasoning.\n\n"
                            "### Ingredients\n"
                            "- 1 whole chicken (approx. 1.5 - 2 kg)\n"
                            "- 2 tbsp unsalted butter, softened\n"
                            "- 1 whole lemon, halved\n"
                            "- 4 garlic cloves, smashed\n"
                            "- Fresh thyme and rosemary sprigs\n"
                            "- Coarse kosher salt and freshly ground black pepper\n\n"
                            "### Instructions\n"
                            "1. **Prep:** Preheat oven to 220°C (425°F). Pat the chicken completely dry with paper towels (essential for crispy skin).\n"
                            "2. **Season:** Generously season the cavity with salt and pepper. Stuff with lemon halves, garlic, and herbs. Rub softened butter all over the skin, then season the outside generously with salt and pepper.\n"
                            "3. **Roast:** Place breast-side up in a roasting pan. Roast for 50-60 minutes, or until the thickest part of the thigh reads 74°C (165°F) on an instant-read thermometer.\n"
                            "4. **Rest:** Remove from oven and let rest for 15 minutes before carving."
                        ),
                        "is_published": True
                    }
                ]
            },
            {
                "category_title": "Health & Fitness",
                "category_body": "Science-backed strategies for physical activity, cardiovascular health, sleep hygiene, and holistic wellness.",
                "notes": [
                    {
                        "title": "The Importance of Sleep Hygiene",
                        "body": (
                            "Quality sleep is just as important for overall health as nutrition and exercise. Sleep hygiene refers to the practices and habits that facilitate good night's rest.\n\n"
                            "### Tips for Better Sleep\n"
                            "1. **Consistent Schedule:** Go to bed and wake up at the same time every day, even on weekends.\n"
                            "2. **Screen-free Wind Down:** Turn off electronic devices (phones, TVs, computers) at least 60 minutes before bedtime.\n"
                            "3. **Cool and Dark Environment:** Keep your bedroom cool (around 18°C / 65°F) and pitch dark or use an eye mask.\n"
                            "4. **Limit Stimulants:** Avoid caffeine or heavy meals in the late afternoon and evening."
                        ),
                        "is_published": True
                    },
                    {
                        "title": "Guidelines for Hydration",
                        "body": (
                            "Water is essential for every single cell in your body. Staying hydrated supports cognitive function, physical performance, and digestion.\n\n"
                            "### Daily Requirements\n"
                            "- As a general rule of thumb, aim for about 2.5 to 3.5 liters of fluids per day.\n"
                            "- Adjust intake based on temperature, humidity, and physical activity levels.\n\n"
                            "### Signs of Dehydration\n"
                            "- Dark urine (ideally, it should be pale straw-colored).\n"
                            "- Dry mouth, fatigue, or mild headaches.\n"
                            "- Decreased cognitive focus."
                        ),
                        "is_published": True
                    }
                ]
            }
        ]

        # Seed data
        for cat_data in seed_data:
            category = Category.objects.create(
                title=cat_data["category_title"],
                body=cat_data["category_body"]
            )
            self.stdout.write(self.style.SUCCESS(f"Created Category: '{category.title}'"))
            
            for note_data in cat_data["notes"]:
                note = Note.objects.create(
                    title=note_data["title"],
                    body=note_data["body"],
                    is_published=note_data["is_published"],
                    category=category
                )
                self.stdout.write(self.style.SUCCESS(f"  -> Created Note: '{note.title}'"))

        self.stdout.write(self.style.SUCCESS("\nDatabase seeding completed successfully!"))
