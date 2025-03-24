# Day 1: Introduction to HTML

## What is HTML?
HTML (HyperText Markup Language) is the standard language for creating web pages. It structures content using elements enclosed in tags.

## 📌 Day 1: HTML Fundamentals  

### Step 1: Setting Up Your First HTML Page  
- Open **VS Code**.  
- Create a new folder named **HTML-Learning** and open it in VS Code.  
- Create a new file named **index.html**. 
- Write the basic HTML structure. 

#### Example Code:
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>My First HTML Page</title>
</head>
<body>
    <h1>Welcome to My First HTML Page</h1>
    <p>This is my first step in learning HTML.</p>
</body>
</html>

### Step 2: Headings & Paragraphs  
- Use `<h1>` to `<h6>` for headings.  
- Use `<p>` for paragraphs.    

#### Example Code:
<h1>Main Heading</h1>
<h2>Subheading</h2>
<p>This is a paragraph of text describing my HTML learning journey.</p>

### Step 3: Lists & Links  
- Create an **unordered list** with `<ul>` and `<li>`.  
- Create an **ordered list** with `<ol>` and `<li>`.  
- Add **links** using `<a href="URL">Link Text</a>`.  

#### Example Code:
<h2>My Favorite Activities</h2>
<ul>
    <li>Reading</li>
    <li>Coding</li>
    <li>Playing Football</li>
</ul>

<h2>My Learning Schedule</h2>
<ol>
    <li>HTML Basics</li>
    <li>CSS Fundamentals</li>
    <li>JavaScript Introduction</li>
</ol>

<h2>Useful Resources</h2>
<a href="https://www.w3schools.com" target="_blank">Visit W3Schools</a>

### Step 4: Adding Images  
- Use `<img src="image.jpg" alt="description">` to display images.  

#### Example Code:
<h2>My Profile Picture</h2>
<img src="profile.jpg" alt="My Profile Picture" width="200">

### Step 5: Creating Tables  
- Use `<table>`, `<tr>`, `<th>`, and `<td>` to organize data in tabular format.  
- Create a table displaying your learning schedule.  
- Add columns for **Day**, **Topic**, and **Status**.  
- Use table rows to represent different days of learning.  
- Ensure that the table has a visible border for better readability.  
- Each row should contain data corresponding to a specific day.  
- Use table headers to label each column.  
- Save and refresh your browser to see the changes. 

#### Example Code:
<h2>My Learning Schedule</h2>
<table border="1">
    <tr>
        <th>Day</th>
        <th>Topic</th>
        <th>Status</th>
    </tr>
    <tr>
        <td>1</td>
        <td>HTML Basics</td>
        <td>Completed</td>
    </tr>
    <tr>
        <td>2</td>
        <td>CSS Basics</td>
        <td>In Progress</td>
    </tr>
</table>

### Step 6: Creating Forms  
- Use `<form>` with `<input>`, `<textarea>`, and `<button>` to collect user input.   
- Create a form for users to input their contact details.  
- Add fields for **Name**, **Email**, and **Message**.  
- Use labels to describe each input field.  
- Ensure the name and email fields are required.  
- Use a textarea for the message input.  
- Add a submit button to complete the form.  
- Save and refresh your browser to test the form.  

#### Example Code:
<h2>Contact Me</h2>
<form>
    <label for="name">Name:</label>
    <input type="text" id="name" name="name" required>
    <br><br>

    <label for="email">Email:</label>
    <input type="email" id="email" name="email" required>
    <br><br>

    <label for="message">Message:</label><br>
    <textarea id="message" name="message" rows="4" cols="30"></textarea>
    <br><br>

    <button type="submit">Send</button>
</form>

### Step 7: Semantic HTML  
- Use `<header>`, `<nav>`, `<section>`, `<article>`, `<aside>`, and `<footer>` for better content structure.  
- Replace `<div>` elements with appropriate semantic HTML tags.  
- Use `<header>` for the top section (title or navigation).  
- Use `<nav>` for navigation menus.  
- Use `<section>` for main content areas.  
- Use `<article>` for independent content like blog posts.  
- Use `<aside>` for side content like a sidebar or ads.  
- Use `<footer>` for the bottom section, like contact info or copyright.  
- Save and refresh your browser to see the improved structure.  

#### Example Code:
<header>
    <h1>Welcome to My Website</h1>
</header>

<nav>
    <ul>
        <li><a href="#">Home</a></li>
        <li><a href="#">About</a></li>
        <li><a href="#">Contact</a></li>
    </ul>
</nav>

<section>
    <h2>My Learning Journey</h2>
    <p>I am learning HTML and web development.</p>
</section>

<footer>
    <p>&copy; 2025 My Website</p>
</footer>

### 🏆 Mini-Project: Personal Profile Page  
- Implement everything learned to create a **personal profile page**.  

#### Requirements:
- A header with your name and a short description.
- A section listing your hobbies or skills.
- An image (your profile picture or a placeholder).
- A contact form for visitors to message you.
- A footer with a copyright notice.

#### Example Code:
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>My Profile</title>
</head>
<body>
    <header>
        <h1>John Doe</h1>
        <p>Web Developer & Designer</p>
    </header>

    <section>
        <h2>About Me</h2>
        <p>I love coding, designing, and building web applications.</p>
    </section>

    <img src="profile.jpg" alt="John's Picture" width="200">

    <section>
        <h2>Contact Me</h2>
        <form>
            <label for="name">Name:</label>
            <input type="text" id="name" name="name" required>
            <br><br>

            <label for="email">Email:</label>
            <input type="email" id="email" name="email" required>
            <br><br>

            <textarea id="message" name="message" rows="4" cols="30"></textarea>
            <br><br>

            <button type="submit">Send</button>
        </form>
    </section>

    <footer>
        <p>&copy; 2025 John Doe</p>
    </footer>
</body>
</html>