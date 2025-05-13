<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  
  <link rel="stylesheet" href="styles.css">
</head>
<body>
  <header>
    <div class="container">
      <h1 class="red"><center>AGIE'S FAST FOODS</center></h1>
      <nav>
        <ul>
          <li><a href="#about">About</a></li>
          <li><a href="#menu">Menu</a></li>
<li><a href="#order">Order Online</a></li>
    <li><a href="#contact">Contact</a></li>
        </ul>
      </nav>
    </div>
  </header>

  <section id="about" class="section">
    <div class="container">
      <h2>About Us</h2>
      <p>Welcome to our restaurant! We serve a wide variety of delicious dishes made with fresh ingredients. We also make deliveries to people around</p>
    </div>
  </section>

  <section id="menu" class="section">
    <div class="container">
      <h2>Our Menu</h2>
      <ul><center><b>SNACKS</b></center>
        <li> Spanish Omlet- 3,000/=</li>
        <li>Sausage {pair}- 3,000/=</li>
        <li>Liver- 7,000/=</li>
        <li>Chapati - 1,000/=</li>
        <li>Madazi - 1,000/=</li>
        <li>Pizza - 30,000/=</li>
        <li>Chips plain - 7,000/=</li>
        <li>Chips Chicken - 15,000/=</li>
        <li>Chips Beef - 12,000/=</li>
       <li>Chips  Fish - 30,000/=</li>     
 </ul>
 <ul><center><b>SOFT DRINKS</b></center>
        <li> Mango juice - 3,000/=</li>
        <li>Pizza - 30,000/=</li>
        <li>Mixed juice - 5,000/=</li>
        <li>Watermelon juice - 3,000/=</li>
        <li>Lemon juice - 3,000/=</li>
        <li>Passion juice - 3,000/=</li>
        <li>Water {big} - 2,500/=</li>
        <li>Water {small} - 1,500/=</li>
        <li>Minute maid - 3,000/=</li>
        <li>Friuts - 5,000/=</li>
       <li>Soda - 2,000/=</li>
       <li>Yoghurt - 2,000/=</li>     
 </ul>
<ul><center><b>LUNCH</b></center>
        <li> Goat meat - 12,000/=</li>
        <li>Chicken - 15,000/=</li>
        <li>Beef - 8,000/=</li>
        <li>G.nuts - 5,000/=</li>
        <li>Beans - 5,000/=</li>
        <li>Peas - 5,000/=</li>
        <li>Fish - 12,000/=</li>
</ul>
<ul><center><b>HOT BEVERAGES</b></center>
        <li> African Tea - 2,000/=</li>
        <li>Black Tea - 2,000/=</li>
        <li>Cofee - 2,000/=</li>
        <li>Dawa Tea - 3,000/=</li>
</ul>
<ul><center><b>KATOGO</b></center>
        <li>Katogo beans - 5,000/=</li>
        <li>Katogo beef- 5,000/=</li>
        <li>Katogo offals- 5,000/=</li>
</ul>
    </div>
  </section>
 </section>
<section id="order" class="section">
    <h2>Order Online</h2>
    <form action="/submit-order" method="POST" class="order-form">
     <label for="name">Your Name:</label>
      <input type="text" id="name" name="name" placeholder="Enter your name" required>
 <label for="phone">Phone Number:</label>
      <input type="tel" id="phone" name="phone" placeholder="Enter your phone number" required>
 <label for="menu-item">Select Menu Item:</label>
      <select id="menu-item" name="menu-item" required>
        <option value="pizza">Pizza - $12</option>
        <option value="pasta">Pasta - $10</option>
        <option value="burger">Burger - $8</option>
        <option value="salad">Salad - $6</option>
      </select>
t<label for="quantity">Quantity:</label>
      <input type="number" id="quantity" name="quantity" min="1" placeholder="Enter quantity" required>
 <label for="address">Delivery Address:</label>
      <textarea id="address" name="address" placeholder="Enter your delivery address" required></textarea>
 <button type="submit">Place Order</button>
    </form>
  </section>
<section id="contact" class="section">
    <div class="container">
      <h2>Contact Us</h2>
      <p>Address: 123 Food Street, Mbarara City</p>
      <p>Phone: (256)706557113/(256)788250403</p>
      <p>Email: brunoamanyire@gmail.com</p>
    </div>
  </section>

  <footer>
    <div class="container">
      <p>&copy; AGIE'S FAST FOODS. All rights reserved.</p>
    </div>
  </footer>
</body>
</html>
