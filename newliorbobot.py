import telebot
from telebot import types

TOKEN = '7578507822:AAHaYiqG5OR-JccrfR8TiAJxC1IYrnTOR1c'  # Replace with your actual bot token
bot = telebot.TeleBot(TOKEN)

# Start message and main buttons
@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(row_width=2)
    products_btn = types.KeyboardButton("Products 🛒")
    help_btn = types.KeyboardButton("Help 📞")
    follow_us_btn = types.KeyboardButton("Follow Us 📲")
    markup.add(products_btn, help_btn, follow_us_btn)
    bot.send_message(message.chat.id, "Welcome to Lior Design! How can we assist you today?", reply_markup=markup)

# Help button handler
@bot.message_handler(func=lambda message: message.text == "Help 📞")
def help(message):
    bot.send_message(message.chat.id, "For support, please contact us via phone number: 0909420082 or reach out to our support team at @Liordesign1.")
    
from telebot import types

# Follow Us button handler
@bot.message_handler(func=lambda message: message.text == "Follow Us 📲")
def follow_us(message):
    markup = types.InlineKeyboardMarkup(row_width=1)
    telegram_btn = types.InlineKeyboardButton("Telegram @Liordesign1", url="https://t.me/Liordesign")
    facebook_btn = types.InlineKeyboardButton("Facebook", url="https://www.facebook.com/profile.php?id=100088499067072&mibextid=ZbWKwL")
    instagram_btn = types.InlineKeyboardButton("Instagram", url="https://www.instagram.com/lior_designs_?igsh=YmpjdmN5djhxcWNr")
    tiktok_btn = types.InlineKeyboardButton("TikTok", url="https://www.tiktok.com/@lior.designs")
    back_btn = types.KeyboardButton("Back 🔙")
    markup.add(telegram_btn, facebook_btn, instagram_btn, tiktok_btn)
    bot.send_message(message.chat.id, "Follow us on our social media platforms:", reply_markup=markup)

# Product buttons handler
@bot.message_handler(func=lambda message: message.text == "Products 🛒")
def products(message):
    markup = types.ReplyKeyboardMarkup(row_width=2)
    lights_btn = types.KeyboardButton("Lights 💡")
    shelves_btn = types.KeyboardButton("Shelves 📚")
    wall_art_btn = types.KeyboardButton("Wall Art & Sculptures 🖼️")
    planters_btn = types.KeyboardButton("Planters 🌱")
    back_btn = types.KeyboardButton("Back 🔙")
    markup.add(lights_btn, shelves_btn, wall_art_btn, planters_btn, back_btn)
    bot.send_message(message.chat.id, "Choose a category:", reply_markup=markup)

@bot.message_handler(func=lambda message: message.text == "Lights 💡")
def lights(message):
    markup = types.ReplyKeyboardMarkup(row_width=1)
    back_btn = types.KeyboardButton("Back 🔙")
    markup.add(back_btn)

    # Lights list with images and upgraded product codes
    bot.send_photo(message.chat.id, "https://postimg.cc/Bjtf4pMf", caption="Wall Mounted Light\nETB 1300\nProduct Code: LIGHT-001")
    bot.send_photo(message.chat.id, "https://postimg.cc/wRJ3fHRF", caption="Wall Mounted Light\nETB 1300\nProduct Code: LIGHT-002")
    bot.send_photo(message.chat.id, "https://postimg.cc/fJcJYzNR", caption="Nordic Bird Design\nETB 1500\nProduct Code: LIGHT-003")
    bot.send_photo(message.chat.id, "https://postimg.cc/qzT7JP3V", caption="Flower Shaped Light\nETB 1800\nProduct Code: LIGHT-004")
    bot.send_photo(message.chat.id, "https://postimg.cc/jCzsFMk8", caption="Light Design\nETB 2000\nProduct Code: LIGHT-005")
    bot.send_photo(message.chat.id, "https://postimg.cc/8FJGB46m", caption="Pendant Light Design for Table\nETB 1800\nProduct Code: LIGHT-006")
    bot.send_photo(message.chat.id, "https://postimg.cc/kDF2bM9X", caption="Pendant Light Design for Table (each)\nETB 1500\nProduct Code: LIGHT-007")
    bot.send_photo(message.chat.id, "https://postimg.cc/9rLzLxr6", caption="Pendant Light Design for Table (3 Lights)\nETB 6000\nProduct Code: LIGHT-008")
    bot.send_photo(message.chat.id, "https://postimg.cc/BL5nHprw", caption="Dynamic Lampshade for Table\nETB 8500\nProduct Code: LIGHT-009")
    bot.send_photo(message.chat.id, "https://postimg.cc/r0T8VWDG", caption="Pendant Light for Kitchen Table\nETB 1400\nProduct Code: LIGHT-010")
    bot.send_photo(message.chat.id, "https://postimg.cc/CRvDfhGf", caption="Orbit Pendant Light Design\nETB 1800\nProduct Code: LIGHT-011")
    bot.send_photo(message.chat.id, "https://postimg.cc/RNhnx55S", caption="Bed Side Standing Light with 3 Light Options\nETB 2500\nProduct Code: LIGHT-012")
    bot.send_photo(message.chat.id, "https://postimg.cc/21wpQJyW", caption="Standing Light Organic Design (1 meter)\nETB 3500\nProduct Code: LIGHT-013")
    bot.send_photo(message.chat.id, "https://postimg.cc/f3p8mjcX", caption="Pendant Light (each)\nETB 1500\nProduct Code: LIGHT-014")

    # Include order instructions
    bot.send_message(
        message.chat.id, 
        "To order, please send the product code to our support team at @Liordesign1.", 
        reply_markup=markup)
    
@bot.message_handler(func=lambda message: message.text == "Shelves 📚")
def shelves(message):
    markup = types.ReplyKeyboardMarkup(row_width=1)
    back_btn = types.KeyboardButton("Back 🔙")
    markup.add(back_btn)

    # List of shelves with images, prices, and upgraded product codes
    bot.send_photo(
        message.chat.id, 
        "https://postimg.cc/VSJdVZNS", 
        caption="Dynamic Shelves (3 pieces)\nETB 2100\nProduct Code: SHELF-001"
    )
    bot.send_photo(
        message.chat.id, 
        "https://postimg.cc/HcGsPpKK", 
        caption="Bird Shaped Shelves (5 pieces)\nETB 3500\nProduct Code: SHELF-002"
    )
    bot.send_photo(
        message.chat.id, 
        "https://postimg.cc/4mptL9gn", 
        caption="60cm Width Shelf (5 pieces)\nETB 4500\nProduct Code: SHELF-003"
    )
    bot.send_photo(
        message.chat.id, 
        "https://postimg.cc/GHMBSJfL", 
        caption="S-Shelf (1 meter * 15cm depth, 3 pieces)\nETB 4000\nProduct Code: SHELF-004"
    )
    bot.send_photo(
        message.chat.id, 
        "https://postimg.cc/n9rxs7G2", 
        caption="Dynamic Book Shelves (3 pieces)\nETB 4000\nProduct Code: SHELF-005"
    )
    bot.send_photo(
        message.chat.id, 
        "https://postimg.cc/1nNcy7Lr", 
        caption="Office Shelf (1 meter * 15cm)\nETB 2500\nProduct Code: SHELF-006"
    )
    bot.send_photo(
        message.chat.id, 
        "https://postimg.cc/XpyPJQ0q", 
        caption="Dynamism as TV Stand & Shelf (4 pieces)\nETB 6000\nProduct Code: SHELF-007"
    )
    bot.send_photo(
        message.chat.id, 
        "https://postimg.cc/G8X2Sv3w", 
        caption="Curves on Shelves (1 meter * 15cm depth)\nETB 4500\nProduct Code: SHELF-008"
    )
    bot.send_photo(
        message.chat.id, 
        "https://postimg.cc/wthFJjqs", 
        caption="1m * 15cm Shelf\nETB 2000\nProduct Code: SHELF-009"
    )
    bot.send_photo(
        message.chat.id, 
        "https://postimg.cc/47jdgscB", 
        caption="Dual Purpose Shelves (1m * 10cm, 2 pieces)\nETB 3000\nProduct Code: SHELF-010"
    )
    bot.send_photo(
        message.chat.id, 
        "https://postimg.cc/mcCRHC1N", 
        caption="Corner Shelves (1m * 15cm, 50cm to right & left, 3 pieces)\nETB 4000\nProduct Code: SHELF-011"
    )
    bot.send_photo(
        message.chat.id, 
        "https://postimg.cc/dkcWhTGC", 
        caption="Column Shelves (7 pieces)\nETB 6500\nProduct Code: SHELF-012"
    )

    # Include order instructions
    bot.send_message(
        message.chat.id, 
        "To order, please send the product code to our support team at @Liordesign1.", 
        reply_markup=markup
    )

@bot.message_handler(func=lambda message: message.text == "Wall Art & Sculptures 🖼️")
def wall_art(message):
    markup = types.ReplyKeyboardMarkup(row_width=1)
    back_btn = types.KeyboardButton("Back 🔙")
    markup.add(back_btn)

    # List of wall art and sculptures with images and prices
    bot.send_photo(
        message.chat.id, 
        "https://postimg.cc/JGL6mpwz", 
        caption="Golden-Silver Corner Art\n#1. 60-70 pieces: ETB 3800\n#2. 90-100 pieces: ETB 4500\n#3. 120-130 pieces: ETB 6000\nProduct Code: WA001"
    )
    bot.send_photo(
        message.chat.id, 
        "https://postimg.cc/Z9ds42q0", 
        caption="Circular Dispersion Wall Art\n#1. 60-70 pieces: ETB 3800\n#2. 90-100 pieces: ETB 4500\n#3. 120-130 pieces: ETB 6000\nProduct Code: WA002"
    )
    bot.send_photo(
        message.chat.id, 
        "https://postimg.cc/9wWLPfYq", 
        caption="Dispersion Wall Art Behind TV\n#1. 60-70 pieces: ETB 3500\n#2. 90-100 pieces: ETB 4000\n#3. 120-130 pieces: ETB 5500\nProduct Code: WA003"
    )
    bot.send_photo(
        message.chat.id, 
        "https://postimg.cc/GBGKZDMy", 
        caption="Dispersion - Gradient Wall Art\n#1. 60-70 pieces: ETB 3500\n#2. 90-100 pieces: ETB 4000\n#3. 120-130 pieces: ETB 5500\nProduct Code: WA004"
    )
    bot.send_photo(
        message.chat.id, 
        "https://postimg.cc/w362G7D1", 
        caption="Dispersion - Corner Wall Art\n#1. 60-70 pieces: ETB 3500\n#2. 90-100 pieces: ETB 4000\n#3. 120-130 pieces: ETB 5500\nProduct Code: WA005"
    )
    bot.send_photo(
        message.chat.id, 
        "https://postimg.cc/8FQBB51P", 
        caption="Circular Blooming Sculptures (Golden-Silver)\n#1. 60-70 pieces: ETB 3800\n#2. 90-100 pieces: ETB 4500\n#3. 120-130 pieces: ETB 6000\nProduct Code: WA006"
    )
    bot.send_photo(
        message.chat.id, 
        "https://postimg.cc/4mjzsdHb", 
        caption="Parametric Golden Wall Art\n80cm*30cm: ETB 4500\n1m*30cm: ETB 5000\n1.5m*35cm: ETB 6000\nProduct Code: WA007"
    )
    bot.send_photo(
        message.chat.id, 
        "https://postimg.cc/rRKrLX8P", 
        caption="Golden Wall Art\n80cm*30cm: ETB 4500\n1m*30cm: ETB 5000\n1.5m*35cm: ETB 6000\nProduct Code: WA008"
    )
    bot.send_photo(
        message.chat.id, 
        "https://postimg.cc/CZ7BBL52", 
        caption="Circle Art for Dining Table\n#1. 1.5m*35cm: ETB 5200\n#2. 2m*35cm (height coverage): ETB 6500\nProduct Code: WA009"
    )
    bot.send_photo(
        message.chat.id, 
        "https://postimg.cc/1fF80K4w", 
        caption="Twisted Wall Sculptures (Black-Golden)\n1.2m height: ETB 5400\nProduct Code: WA010"
    )
    bot.send_photo(
        message.chat.id, 
        "https://postimg.cc/YLrJjVFX", 
        caption="Fine Arts & Sculptures\nETB 1200\nProduct Code: WA011"
    )
    bot.send_photo(
        message.chat.id, 
        "https://postimg.cc/K4f6CGXC", 
        caption="Fine Arts & Sculptures\nETB 1200\nProduct Code: WA012"
    )
    bot.send_photo(
        message.chat.id, 
        "https://postimg.cc/SJKBhBkR", 
        caption="Human Figure Sculptures\nETB 1800\nProduct Code: WA013"
    )
    bot.send_photo(
        message.chat.id, 
        "https://postimg.cc/gxCQ3rRL", 
        caption="Bicycle Sculpture\nETB 1500\nProduct Code: WA014"
    )
    bot.send_photo(
        message.chat.id, 
        "https://postimg.cc/sQyL08TV", 
        caption="Mother & Son Sculpture\nETB 1500\nProduct Code: WA015"
    )
    bot.send_photo(
        message.chat.id, 
        "https://postimg.cc/k6cHrcHW", 
        caption="Flamingo Sculptures\nETB 1500\nProduct Code: WA016"
    )

    # Include order instructions
    bot.send_message(
        message.chat.id, 
        "To order, please send the product code to our support team at @Liordesign1.", 
        reply_markup=markup
    )

@bot.message_handler(func=lambda message: message.text == "Planters 🌱")
def planters(message):
    markup = types.ReplyKeyboardMarkup(row_width=1)
    back_btn = types.KeyboardButton("Back 🔙")
    markup.add(back_btn)

    # Twisted Planter
    bot.send_photo(
        message.chat.id, 
        "https://postimg.cc/56ZnRTtZ",  # Twisted Planter image
        caption="Twisted Planter\nETB 800\nProduct Code: PLANTER-001"
    )
    
    # Cone Planter #1 Without background
    bot.send_photo(
        message.chat.id, 
        "https://postimg.cc/nsxTHmB2",  # Cone Planter #1 Without background image
        caption="Cone Planters #1 (Without background)\nETB 600\nProduct Code: PLANTER-002"
    )
    
    # Cone Planter #2 With background plate
    bot.send_photo(
        message.chat.id, 
        "https://postimg.cc/18wJhBn4",  # Cone Planter #2 With background plate image
        caption="Cone Planters #2 (With background plate)\nETB 800\nProduct Code: PLANTER-003"
    )
    
    # Small Sized for Cactus Plant
    bot.send_photo(
        message.chat.id, 
        "https://postimg.cc/7GYVzyBT",  # Small Sized for Cactus Plant image
        caption="Small Sized for Cactus Plant\nETB 500\nProduct Code: PLANTER-004"
    )
    
    # Bigger Sized for Cactus Plant
    bot.send_photo(
        message.chat.id, 
        "https://postimg.cc/dZhjWjcs",  # Bigger Sized for Cactus Plant image
        caption="Bigger Sized for Cactus Plant\nETB 700\nProduct Code: PLANTER-005"
    )
    
    # Planter Design #6
    bot.send_photo(
        message.chat.id, 
        "https://postimg.cc/SjRdNk2B",  # Planter Design #6 image
        caption="Planter Design #6\nETB 500\nProduct Code: PLANTER-006"
    )
    
    # Planter Design #7
    bot.send_photo(
        message.chat.id, 
        "https://postimg.cc/vDKz4k5c",  # Planter Design #7 image
        caption="Planter Design #7\nETB 700\nProduct Code: PLANTER-007"
    )

    # Planter Design #8
    bot.send_photo(
        message.chat.id, 
        "https://postimg.cc/3k5FBGSh",  # Planter Design #8 image
        caption="Planter Design #8\nETB 400\nProduct Code: PLANTER-008"
    )
    
    # Planter Design #9 (2 pieces)
    bot.send_photo(
        message.chat.id, 
        "https://postimg.cc/mPYN6rJH",  # Planter Design #9 (2 pieces) image
        caption="Planter Design #9 (2 pieces)\nETB 600\nProduct Code: PLANTER-009"
    )
    
    # Planter Design #10
    bot.send_photo(
        message.chat.id, 
        "https://postimg.cc/t19t0jGm",  # Planter Design #10 image
        caption="Planter Design #10\nETB 1500\nProduct Code: PLANTER-010"
    )
    
    # Wine Rack Design Planter
    bot.send_photo(
        message.chat.id, 
        "https://postimg.cc/0MBpJKML",  # Wine Rack Design image
        caption="Wine Rack Design (Suitable for kitchen & dining table)\nETB 2000\nProduct Code: PLANTER-011"
    )

    # Order instructions
    bot.send_message(
        message.chat.id, 
        "To order, please send the product code to our support team at @Liordesign1.", 
        reply_markup=markup
    )
    
# Back button handler
@bot.message_handler(func=lambda message: message.text == "Back 🔙")
def back(message):
    start(message)

# Run the bot
bot.polling()