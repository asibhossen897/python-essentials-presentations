from seleniumbase import BaseCase

BaseCase.main(__name__, __file__)

class MyTestClass(BaseCase):
    def test_presentation(self):
        self.create_presentation(theme="serif", transition="fade")
        
        self.add_slide(
            "<h2>Python Essentials:</h2>\n"
            "<h3>Fundamentals and Practical Projects for Beginners</h3>"
            "<hr /><br />\n"
            "<hd>Presented by <b>Asib Hossen</b></h4>\n"
            "<h4>Incieto Institute - 2024</h4>\n"
        )
        
        # Module 0: Welcome and Prerequisites
        self.add_slide(
            "<h2>Module 0:</h2>\n"
            "<hr /><br />\n"
            "<h3>Welcome and Prerequisites</h3>"
        )
        self.add_slide(
            "<h3>Assalamu'alaikum!</h3>"
            "<h3>Welcome to the course!</h3>"
        )
        self.add_slide(
            "<h3>Introduction of the Instructor:</h3>"
            "<p>Presented by Asib Hossen</p>\n"
        )
        self.add_slide(
            "<h3>Why is this course here anyway?</h3>"
            "<hr /><br />\n"
            "<p>To teach Python essentials and practical projects for beginners.</p>\n"
        )
        self.add_slide(
            "<h3>What do you need to know about to get up and running with this course?</h3>"
            "<hr /><br />\n"
            "<p>No prerequisites required.</p>\n"
        )

        # Module 1: Python Fundamentals
        self.add_slide(
            "<h2>Module 1:</h2>\n"
            "<hr /><br />\n"
            "<h3>Python Fundamentals</h3>"
        )
        self.add_slide(
            "<h3>Lesson 1: Introduction to Python</h3>"
            "<hr /><br />\n"
            "<ul>\n"
            "<li><mk-0>Overview of Python programming language.</mk-0></li>\n"
            "<li><mk-1>Setting up a Cloud Python Environment.</mk-1></li>\n"
            "<li><mk-2>Setting up a Local Python environment.</mk-2></li>\n"
            "<li><mk-3>Writing and running a basic Python script.</mk-3></li>\n"
            "</ul>\n"
        )
        self.add_slide(
            "<h3>Lesson 2: Variables and Data Types</h3>"
            "<hr /><br />\n"
            "<ul>\n"
            "<li><mk-0>Understanding variables and data types (integers, floats, strings).</mk-0></li>\n"
            "<li><mk-1>Understanding Lists, Sets, and Dictionaries.</mk-1></li>\n"
            "<li><mk-2>Performing basic operations with variables.</mk-2></li>\n"
            "<li><mk-3>String manipulation techniques.</mk-3></li>\n"
            "</ul>\n"
        )
        self.add_slide(
            "<h3>Lesson 3: Control Flow: Conditional Statements and Loops</h3>"
            "<hr /><br />\n"
            "<ul>\n"
            "<li><mk-0>Introduction to conditional statements (if, elif, else).</mk-0></li>\n"
            "<li><mk-1>Working with loops (for loop, while loop).</mk-1></li>\n"
            "<li><mk-2>Practical examples including factorial calculation and simple condition checking.</mk-2></li>\n"
            "</ul>\n"
        )
        self.add_slide(
            "<h3>Lesson 4: Functions and Modules</h3>"
            "<hr /><br />\n"
            "<ul>\n"
            "<li><mk-0>Defining and calling functions.</mk-0></li>\n"
            "<li><mk-1>Parameters and Arguments.</mk-1></li>\n"
            "<li><mk-2>Introduction to Python modules.</mk-2></li>\n"
            "<li><mk-3>Exploring the math module for mathematical operations.</mk-3></li>\n"
            "</ul>\n"
        )
        self.add_slide(
            "<h3>Lesson 5: Error Handling</h3>"
            "<hr /><br />\n"
            "<ul>\n"
            "<li><mk-0>Understanding common errors in Python.</mk-0></li>\n"
            "<li><mk-1>Using try-except blocks for error handling.</mk-1></li>\n"
            "<li><mk-2>Handling specific exceptions.</mk-2></li>\n"
            "</ul>\n"
        )
        self.add_slide(
            "<h3>Lesson 6: File Handling</h3>"
            "<hr /><br />\n"
            "<ul>\n"
            "<li><mk-0>Reading from and writing to files in Python.</mk-0></li>\n"
            "<li><mk-1>Opening files in different modes (read, write, append).</mk-1></li>\n"
            "<li><mk-2>Practical exercises with file handling operations.</mk-2></li>\n"
            "</ul>\n"
        )

        # Module 2: Web Scraping Fundamentals with Requests and BeautifulSoup
        self.add_slide(
            "<h2>Module 2:</h2>\n"
            "<hr /><br />\n"
            "<h3>Web Scraping Fundamentals with Requests and BeautifulSoup</h3>"
        )
        self.add_slide(
            "<h3>Lesson 1: Introduction to Web Scraping</h3>"
            "<hr /><br />\n"
            "<ul>\n"
            "<li><mk-0>Overview of web scraping and its applications.</mk-0></li>\n"
            "<li><mk-1>Ethical considerations and legal implications.</mk-1></li>\n"
            "</ul>\n"
        )
        self.add_slide(
            "<h3>Lesson 2: Understanding HTML and CSS basics</h3>"
            "<hr /><br />\n"
            "<ul>\n"
            "<li><mk-0>Basic structure of HTML documents.</mk-0></li>\n"
            "<li><mk-1>Introduction to CSS selectors.</mk-1></li>\n"
            "</ul>\n"
        )
        self.add_slide(
            "<h3>Lesson 3: Introduction to Requests library</h3>"
            "<hr /><br />\n"
            "<ul>\n"
            "<li><mk-0>Making HTTP requests with Requests.</mk-0></li>\n"
            "<li><mk-1>Handling response objects.</mk-1></li>\n"
            "</ul>\n"
        )
        self.add_slide(
            "<h3>Lesson 4: Parsing HTML with BeautifulSoup</h3>"
            "<hr /><br />\n"
            "<ul>\n"
            "<li><mk-0>Introduction to BeautifulSoup library.</mk-0></li>\n"
            "<li><mk-1>Parsing HTML documents.</mk-1></li>\n"
            "</ul>\n"
        )
        self.add_slide(
            "<h3>Lesson 5: Extracting data from web pages</h3>"
            "<hr /><br />\n"
            "<ul>\n"
            "<li><mk-0>Identifying and extracting specific data elements.</mk-0></li>\n"
            "<li><mk-1>Handling different types of HTML content.</mk-1></li>\n"
            "</ul>\n"
        )
        self.add_slide(
            "<h3>Lesson 6: Handling dynamic content with Selenium (Optional)</h3>"
            "<hr /><br />\n"
            "<ul>\n"
            "<li><mk-0>Introduction to Selenium for web automation.</mk-0></li>\n"
            "<li><mk-1>Handling dynamic content and JavaScript-rendered pages.</mk-1></li>\n"
            "</ul>\n"
        )

        # Module 3: File Downloading and Management
        self.add_slide(
            "<h2>Module 3:</h2>\n"
            "<hr /><br />\n"
            "<h3>File Downloading and Management</h3>"
        )
        self.add_slide(
            "<h3>Lesson 1: Introduction to File Downloading</h3>"
            "<hr /><br />\n"
            "<ul>\n"
            "<li><mk-0>Overview of file downloading with Python.</mk-0></li>\n"
            "<li><mk-1>Applications and use cases.</mk-1></li>\n"
            "</ul>\n"
        )
        self.add_slide(
            "<h3>Lesson 2: Downloading Text Files</h3>"
            "<hr /><br />\n"
            "<ul>\n"
            "<li><mk-0>Using Python to download text files from the web.</mk-0></li>\n"
            "</ul>\n"
        )
        self.add_slide(
            "<h3>Lesson 3: Downloading Images</h3>"
            "<hr /><br />\n"
            "<ul>\n"
            "<li><mk-0>Downloading images from URLs using Python.</mk-0></li>\n"
            "</ul>\n"
        )
        self.add_slide(
            "<h3>Lesson 4: Downloading Documents (PDFs, Word, etc.)</h3>"
            "<hr /><br />\n"
            "<ul>\n"
            "<li><mk-0>Techniques for downloading PDFs, Word documents, and other document formats.</mk-0></li>\n"
            "</ul>\n"
        )
        self.add_slide(
            "<h3>Lesson 5: Downloading Data Files (CSV, Excel, JSON, etc.)</h3>"
            "<hr /><br />\n"
            "<ul>\n"
            "<li><mk-0>Using Python to download structured data files like CSV, Excel, and JSON.</mk-0></li>\n"
            "</ul>\n"
        )
        self.add_slide(
            "<h3>Lesson 6: Advanced File Management</h3>"
            "<hr /><br />\n"
            "<ul>\n"
            "<li><mk-0>Techniques for managing downloaded files.</mk-0></li>\n"
            "</ul>\n"
        )

        # Module 4: Accessing Data from Quran.com API
        self.add_slide(
            "<h2>Module 4:</h2>\n"
            "<hr /><br />\n"
            "<h3>Accessing Data from Quran.com API</h3>"
        )
        self.add_slide(
            "<h3>Lesson 1: Introduction to Quran.com API</h3>"
            "<hr /><br />\n"
            "<ul>\n"
            "<li><mk-0>What is  API?</mk-0></li>\n"
            "<li><mk-1>Overview of Quran.com API and its features.</mk-1></li>\n"
            "<li><mk-2>Understanding the structure of Quranic data provided by the API.</mk-2></li>\n"
            "</ul>\n"
        )
        self.add_slide(
            "<h3>Lesson 2: Making API Requests</h3>"
            "<hr /><br />\n"
            "<ul>\n"
            "<li><mk-0>Using Python libraries to make HTTP requests to the Quran.com API.</mk-0></li>\n"
            "<li><mk-1>Handling API responses and extracting relevant data.</mk-1></li>\n"
            "<li><mk-2>Understanding the structure of Quranic data provided by the API.</mk-2></li>\n"
            "</ul>\n"
        )
        self.add_slide(
            "<h3>Lesson 3: Retrieving Surah Information</h3>"
            "<hr /><br />\n"
            "<ul>\n"
            "<li><mk-0>Retrieving information about specific Surahs (chapters) from the Quran.</mk-0></li>\n"
            "<li><mk-1>Getting Surah Number and Total verses in a Surah and so on.</mk-1></li>\n"
            "</ul>\n"
        )
        self.add_slide(
            "<h3>Lesson 4: Retrieving Ayah Information</h3>"
            "<hr /><br />\n"
            "<ul>\n"
            "<li><mk-0>Retrieving information about individual Ayahs (verses) from the Quran.</mk-0></li>\n"
            "<li><mk-1>Getting Audio, Text and Translation of an Ayah.</mk-1></li>\n"
            "</ul>\n"
        )
        self.add_slide(
            "<h3>Lesson 5: Advanced Queries and Filters</h3>"
            "<hr /><br />\n"
            "<ul>\n"
            "<li><mk-0>Performing advanced queries and filters to retrieve specific Quranic data.</mk-0></li>\n"
            "</ul>\n"
        )
        self.add_slide(
            "<h3>Lesson 6: Integrating Quranic Data into Applications</h3>"
            "<hr /><br />\n"
            "<ul>\n"
            "<li><mk-0>Integrating Quranic data retrieved from the API into applications.</mk-0></li>\n"
            "</ul>\n"
        )

        # Module 5: Practical Practice Projects
        self.add_slide(
            "<h2>Module 5:</h2>\n"
            "<hr /><br />\n"
            "<h3>Practical Practice Projects</h3>"
        )
        self.add_slide(
            "<h3>Project 1: Web Scraping Project</h3>"
            "<hr /><br />\n"
            "<ul>\n"
            "<li><mk-0>Task: Scrape data from a website and store it in a CSV file.</mk-0></li>\n"
            "<li><mk-1>Skills: Using Requests, BeautifulSoup, and file handling.</mk-1></li>\n"
            "</ul>\n"
        )
        self.add_slide(
            "<h3>Project 2: Unsplash Scraping Project</h3>"
            "<hr /><br />\n"
            "<ul>\n"
            "<li><mk-0>Task: Create a program to scrape image URLs and download images from the list of URLs.</mk-0></li>\n"
            "<li><mk-1>Skills: File downloading, error handling.</mk-1></li>\n"
            "</ul>\n"
        )
        self.add_slide(
            "<h3>Project 3: Quran.com API Integration Project</h3>"
            "<hr /><br />\n"
            "<ul>\n"
            "<li><mk-0>Task: Build an application that retrieves Quranic data from Quran.com API and displays it in a user-friendly format.</mk-0></li>\n"
            "<li><mk-1>Skills: Making API requests, data visualization.</mk-1></li>\n"
            "</ul>\n"
        )

        # Save the presentation
        self.save_presentation(filename="python_essentials_course_outline.html")
