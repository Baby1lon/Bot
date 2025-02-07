import telebot
from telebot import types

# Bot token and support team chat ID
TOKEN = '7578507822:AAFNJN9FNJG32HSKqHcdloxOQXMKJxEMYnw'
bot = telebot.TeleBot(TOKEN)
SUPPORT_TEAM_CHAT_ID = '5935726066'

# Function to start the bot and show the main menu
@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)

    # Define the four buttons
    products_button = types.KeyboardButton('🛍️ Explore Products')
    help_button = types.KeyboardButton('❓ Help')
    follow_us_button = types.KeyboardButton('🌍 Follow Us')
    weekly_discount_button = types.KeyboardButton('🎉 Weekly Discount')  # Updated icon

    # Add the buttons in two rows for equal size
    markup.row(products_button, help_button)  # First row
    markup.row(follow_us_button, weekly_discount_button)  # Second row

    # Greet the user with their name if available
    user_name = message.from_user.first_name or "there"
    
    bot.send_message(
        message.chat.id,
        f'Hi {user_name}, welcome to **Lior Design**! 🛋️✨\nChoose an option below to explore our products.',
        reply_markup=markup,
        parse_mode='Markdown'
    )
    
# Function to handle the "Help" button click
@bot.message_handler(func=lambda message: message.text == '❓ Help')
def show_help(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    back_button = types.KeyboardButton('🔙 Back')
    markup.add(back_button)

    # Send phone number and support team contact
    bot.send_message(
        message.chat.id,
        "For any inquiries or assistance, you can reach us at:\n\n"
        "📞 Phone: 0909420082\n"
        "📩 Support Team: @Liordesign1\n\n"
        "Feel free to contact us for help!",
        reply_markup=markup
    )

# Function to handle the "Follow Us" button click
@bot.message_handler(func=lambda message: message.text == '🌍 Follow Us')
def follow_us(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)  # Adjust row width for equal size
    # Social media buttons with direct links
    facebook_button = types.KeyboardButton('🔵 Facebook')
    instagram_button = types.KeyboardButton('📸 Instagram')
    telegram_button = types.KeyboardButton('📱 Telegram')
    tiktok_button = types.KeyboardButton('🎵 TikTok')
    
    # Back button with a callback to go back to the main menu
    back_button = types.KeyboardButton('🔙 Back to Main Menu')

    # Adding social media and back buttons to the main markup
    markup.add(facebook_button, instagram_button, telegram_button, tiktok_button, back_button)

    bot.send_message(
        message.chat.id,
        "Follow us on our social media channels for updates, promotions, and more!",
        reply_markup=markup
    )

# Function to handle the social media button clicks
@bot.message_handler(func=lambda message: message.text == '🔵 Facebook')
def facebook(message):
    bot.send_message(message.chat.id, "Visit our Facebook: https://www.facebook.com/profile.php?id=100088499067072&mibextid=ZbWKwL")

@bot.message_handler(func=lambda message: message.text == '📸 Instagram')
def instagram(message):
    bot.send_message(message.chat.id, "Visit our Instagram: https://www.instagram.com/lior_designs_?igsh=YmpjdmN5djhxcWNr")

@bot.message_handler(func=lambda message: message.text == '📱 Telegram')
def telegram(message):
    bot.send_message(message.chat.id, "Visit our Telegram: https://t.me/Liordesign")

@bot.message_handler(func=lambda message: message.text == '🎵 TikTok')
def tiktok(message):
    bot.send_message(message.chat.id, "Visit our TikTok: https://www.tiktok.com/@lior.designs")

# Function to handle the "Back to Main Menu" button
@bot.message_handler(func=lambda message: message.text == '🔙 Back to Main Menu')
def back_to_main_menu(message):
    send_welcome(message)  # Calling the welcome function to return to the main menu
    
    # Function to handle the "Products" button click
@bot.message_handler(func=lambda message: message.text == '🛍️ Explore Products')
def show_products(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    # Add your product-related buttons here
    # Make sure your button handlers are not nested inside this function
    # For example, you can define more buttons like:
    lights_button = types.KeyboardButton('💡 Lights')
    shelves_button = types.KeyboardButton('📚 Shelves')
    wall_art_button = types.KeyboardButton('🖼️ Wall Art & Sculptures')
    planters_button = types.KeyboardButton('🪴 Planters')
    table_button = types.KeyboardButton('🪑 Tables')
    back_button = types.KeyboardButton('🔙 Back')

    markup.add(lights_button, shelves_button, wall_art_button, planters_button, table_button, back_button)

    bot.send_message(message.chat.id, 'Explore our categories below:', reply_markup=markup)

# Function to handle the "Weekly Discount" button click
@bot.message_handler(func=lambda message: message.text == '🎉 Weekly Discount')
def weekly_discount(message):
    text = (
        "⚠️ *Discount Offer Not Available* ⚠️\n\n"
        "Our exclusive weekly discount is coming soon! 🎉\n"
        "This special offer will be available *only for our followers*.\n\n"
        "📲 *Follow us now to stay updated and be the first to grab the deals!*"
    )

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    follow_button = types.KeyboardButton("🌍 Follow Us")
    back_button = types.KeyboardButton("🔙 Back to Main Menu")
    markup.row(follow_button, back_button)

    bot.send_message(message.chat.id, text, reply_markup=markup, parse_mode="Markdown")

# Function to handle the "Lights" button click
lights_button = types.KeyboardButton('💡 Lights')

@bot.message_handler(func=lambda message: message.text == '💡 Lights') 
def show_lights(message): 
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True) 
    back_button = types.KeyboardButton('🔙 Back') 
    markup.add(back_button)

    products = [
        ("https://postimg.cc/Bjtf4pMf", "Wall mounted light\nPrice: ETB 1300\nProduct Code: Lior-Lights-001"),
        ("https://postimg.cc/wRJ3fHRF", "Wall mounted light\nPrice: ETB 1300\nProduct Code: Lior-Lights-002"),
        ("https://postimg.cc/fJcJYzNR", "Nordic bird design\nPrice: ETB 1500\nProduct Code: Lior-Lights-003"),
        ("https://postimg.cc/qzT7JP3V", "Flower shaped light\nPrice: ETB 1800\nProduct Code: Lior-Lights-004"),
        ("https://postimg.cc/jCzsFMk8", "Lighting design\nPrice: ETB 2000\nProduct Code: Lior-Lights-005"),
        ("https://postimg.cc/8FJGB46m", "Lighting design\nPrice: ETB 1800\nProduct Code: Lior-Lights-006"),
        ("https://postimg.cc/kDF2bM9X", "Lighting design\nPrice: ETB 1500 each\nProduct Code: Lior-Lights-007"),
        ("https://postimg.cc/9rLzLxr6", "Pendant light design for table\n1. 80cm*30cm - 3 lights (warm & white) - ETB 4500\n2. 110cm*30cm - 3 lights - ETB 5500\nProduct Code: Lior-Lights-008"),
        ("https://postimg.cc/BL5nHprw", "Dynamic lampshade for table\n2 meter * 30cm, 5 lights - ETB 8500\nProduct Code: Lior-Lights-009"),
        ("https://postimg.cc/r0T8VWDG", "Pendant light for kitchen table\nCone shaped light - Price: ETB 1400\nProduct Code: Lior-Lights-010"),
        ("https://postimg.cc/CRvDfhGf", "Orbit pendant light design\nPrice: ETB 1800\nProduct Code: Lior-Lights-011"),
        ("https://postimg.cc/RNhnx55S", "Bedside standing light - 3 light options\nPrice: ETB 2500\nProduct Code: Lior-Lights-012"),
        ("https://postimg.cc/21wpQJyW", "Standing light - organic design\n1 meter - ETB 3500\nProduct Code: Lior-Lights-013"),
        ("https://postimg.cc/f3p8mjcX", "Pendant light\nPrice: ETB 1500 each\nProduct Code: Lior-Lights-014")
    ]

    for photo_url, caption in products:
        bot.send_photo(
            message.chat.id, 
            photo_url, 
            caption=caption,
            reply_markup=types.InlineKeyboardMarkup([
                [types.InlineKeyboardButton('🛒 Order Now', callback_data=f'order_{caption.split()[-1]}')]
            ])
        )

    bot.send_message(message.chat.id, "Click 'Order Now' to place your order or 'Back' to return.", reply_markup=markup)

# Function to handle the "Shelves" button click
@bot.message_handler(func=lambda message: message.text == '📚 Shelves')
def show_shelves(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    back_button = types.KeyboardButton('🔙 Back')
    markup.add(back_button)

    shelves = [
        ("https://postimg.cc/VSJdVZNS", "Dynamic shelves\n3 pieces - ETB 2100\n5 pieces - ETB 3500", "Lior-Shelves-001"),
        ("https://postimg.cc/HcGsPpKK", "Bird shaped shelves\n3 pieces - ETB 2100\n5 pieces - ETB 3500", "Lior-Shelves-002"),
        ("https://postimg.cc/4mptL9gn", "60cm width * 15cm depth, 5 pieces\nPrice - ETB 4500", "Lior-Shelves-003"),
        ("https://postimg.cc/GHMBSJfL", "S-shelf\n1 meter * 15cm depth\n3 pieces - ETB 4000", "Lior-Shelves-004"),
        ("https://postimg.cc/8JNHMH5z", "Dynamic book shelves\n1 meter * 15cm depth\n3 pieces - ETB 4000", "Lior-Shelves-005"),
        ("https://postimg.cc/1nNcy7Lr", "Office shelf\n1 meter * 15cm depth\nPrice - ETB 2500", "Lior-Shelves-006"),
        ("https://postimg.cc/XpyPJQ0q", "'Dynamism' as TV stand & Shelf\nOriginal design by Zaha Hadid\n4 pieces - ETB 5500", "Lior-Shelves-007"),
        ("https://postimg.cc/G8X2Sv3w", "Curves on shelves\n1 meter * 15cm depth - ETB 4500\n1.2m * 15cm - ETB 5000", "Lior-Shelves-008"),
        ("https://postimg.cc/wthFJjqs", "1m * 15cm\nPrice - ETB 2000", "Lior-Shelves-009"),
        ("https://postimg.cc/47jdgscB", "Dual purpose shelves\n1m * 10cm, 2 pieces\nPrice - ETB 3000", "Lior-Shelves-010"),
        ("https://postimg.cc/mcCRHC1N", "Corner shelves\n1m * 15cm (50cm to right & left)\n3 pieces - ETB 4000", "Lior-Shelves-011"),
        ("https://postimg.cc/dkcWhTGC", "Column shelves\n7 pieces - ETB 6500", "Lior-Shelves-012"),
        ("https://postimg.cc/CBPj4hmY", "50 cm * 10 cm depth\n3 Pieces - ETB 2200", "Lior-Shelves-013")
    ]

    for image_url, caption, product_code in shelves:
        bot.send_photo(message.chat.id, image_url, caption=caption, reply_markup=types.InlineKeyboardMarkup([
            [types.InlineKeyboardButton('🛒 Order Now', callback_data=f'order_{product_code}')]
        ]))

    bot.send_message(message.chat.id, "Click 'Order Now' to place your order or 'Back' to go back.", reply_markup=markup)

# Function to handle the "Wall Art & Sculptures" button click
@bot.message_handler(func=lambda message: message.text == '🖼️ Wall Art & Sculptures')
def show_wall_art(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    category1_button = types.KeyboardButton('🖼️ Category 1')
    category2_button = types.KeyboardButton('🖼️ Category 2')
    category3_button = types.KeyboardButton('🖼️ Category 3')
    back_button = types.KeyboardButton('🔙 Back')
    
    markup.add(category1_button, category2_button, category3_button, back_button)
    
    bot.send_message(message.chat.id, "Choose a category:", reply_markup=markup)
    
# Function to handle the "Category 1" button click
@bot.message_handler(func=lambda message: message.text == '🖼️ Category 1')
def show_category1(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    back_button = types.KeyboardButton('🔙 Back')
    markup.add(back_button)

    products = [
        ("https://i.postimg.cc/JGL6mpwz/image.jpg", "Golden-Silver Corner Art\n#1. 60-70 pieces - ETB 3800\n#2. 90-100 pieces - ETB 4500\n#3. 120-130 pieces - ETB 6000", "order_Lior-WallArt-001"),
        ("https://i.postimg.cc/6THdNcYT/image.jpg", "Circular Dispersion Wall Art\n#1. 60-70 pieces - ETB 3800\n#2. 90-100 pieces - ETB 4500\n#3. 120-130 pieces - ETB 6000", "order_Lior-WallArt-002"),
        ("https://i.postimg.cc/9wWLPfYq/image.jpg", "Desperation Wall Art Behind TV\n#1. 60-70 pieces - ETB 3500\n#2. 90-100 pieces - ETB 4000\n#3. 120-130 pieces - ETB 5500", "order_Lior-WallArt-003"),
        ("https://i.postimg.cc/GBGKZDMy/image.jpg", "Dispersion - Gradient Wall Art\n#1. 60-70 pieces - ETB 3500\n#2. 90-100 pieces - ETB 4000\n#3. 120-130 pieces - ETB 5500", "order_Lior-WallArt-004"),
        ("https://i.postimg.cc/w362G7D1/image.jpg", "Dispersion - Corner Wall Art\n#1. 60-70 pieces - ETB 3500\n#2. 90-100 pieces - ETB 4000\n#3. 120-130 pieces - ETB 5500", "order_Lior-WallArt-005"),
        ("https://i.postimg.cc/8FQBB51P/image.jpg", "Circular Blooming Sculptures\nGolden-Silver\n#1. 60-70 pieces - ETB 3800\n#2. 90-100 pieces - ETB 4500\n#3. 120-130 pieces - ETB 6000", "order_Lior-WallArt-006"),
        ("https://i.postimg.cc/MnJXkj2v/image.jpg", "Parametric Golden Wall Art\n80cm*30cm - ETB 4500\n1m*30cm - ETB 5000\n1.5m*35cm - ETB 6000", "order_Lior-WallArt-007"),
        ("https://i.postimg.cc/rRKrLX8P/image.jpg", "Golden Wall Art\n80cm*30cm - ETB 4500\n1m*30cm - ETB 5000\n1.5m*35cm - ETB 6000", "order_Lior-WallArt-008"),
        ("https://i.postimg.cc/CZ7BBL52/image.jpg", "Circle Art - For Dining Table\n#1. 1.5m * 35cm - ETB 5200\n#2. 2m * 35cm height coverage - ETB 6500", "order_Lior-WallArt-009"),
        ("https://i.postimg.cc/1fF80K4w/image.jpg", "Twisted Wall Sculptures\nBlack - Golden\n1.2m height - ETB 5400", "order_Lior-WallArt-010"),
        ("https://i.postimg.cc/YLrJjVFX/image.jpg", "Fine Arts & Sculpture\nETB 1200", "order_Lior-WallArt-011")
    ]

    for photo, caption, callback_data in products:
        bot.send_photo(
            message.chat.id,
            photo,
            caption=caption,
            reply_markup=types.InlineKeyboardMarkup([
                [types.InlineKeyboardButton('🛒 Order Now', callback_data=callback_data)]
            ])
        )

    bot.send_message(message.chat.id, "Click 'Order Now' to place your order or 'Back' to go back.", reply_markup=markup)
    
    # Function to handle the "Category 2" button click
@bot.message_handler(func=lambda message: message.text == '🖼️ Category 2')
def show_category2(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    back_button = types.KeyboardButton('🔙 Back')
    markup.add(back_button)

    # List of products with their images, captions (name & price), and order callback data
    products = [
        ("https://postimg.cc/K4f6CGXC", "Product: Frame Art\nPrice: ETB 1200", "order_Lior-WallArt-012"),
        ("https://postimg.cc/SJKBhBkR", "Product: Human Figure Sculptures\nPrice: ETB 1800", "order_Lior-WallArt-013"),
        ("https://postimg.cc/gxCQ3rRL", "Product: Bicycle Sculpture\nPrice: ETB 1500", "order_Lior-WallArt-014"),
        ("https://postimg.cc/sQyL08TV", "Product: Mother & Son Sculpture\nPrice: ETB 1500", "order_Lior-WallArt-015"),
        ("https://postimg.cc/k6cHrcHW", "Product: Flamingo Sculptures\nPrice: ETB 2000", "order_Lior-WallArt-016"),
        ("https://postimg.cc/XXjhfRZL", "Product: Landscape Sculpture\nPrice: ETB 1800", "order_Lior-WallArt-017"),
        ("https://postimg.cc/8js03Lmr", "Product: Dancing Couples\nPrice: ETB 1500", "order_Lior-WallArt-018"),
        ("https://postimg.cc/5HWK6Tdw", "Product: Sufi Dancer Sculpture\nPrice: ETB 1300", "order_Lior-WallArt-019"),
        ("https://postimg.cc/Tyj7m0fB", "Product: Fire Circus\nPrice: ETB 1500", "order_Lior-WallArt-020"),
        ("https://postimg.cc/LYHyVPs5", "Product: Frame Art (70*70cm)\nPrice: ETB 7000", "order_Lior-WallArt-021"),
        ("https://postimg.cc/xJt6pdkR", "Product: The Hug\nPrice: ETB 1500", "order_Lior-WallArt-022"),
    ]

    # Loop through each product and send it as a separate message
    for photo, caption, callback_data in products:
        bot.send_photo(
            message.chat.id,
            photo,
            caption=caption,
            reply_markup=types.InlineKeyboardMarkup([
                [types.InlineKeyboardButton('🛒 Order Now', callback_data=callback_data)]
            ])
        )

    # Send a message with the back button
    bot.send_message(message.chat.id, "Click 'Order Now' to place your order or 'Back' to return.", reply_markup=markup)
    
 # Category 3 products with price and photo code
@bot.message_handler(func=lambda message: message.text == '🖼️ Category 3')
def show_category3(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    back_button = types.KeyboardButton('🔙 Back')
    markup.add(back_button)

    # 3 Pieces Art
    bot.send_photo(
        message.chat.id, 
        "https://postimg.cc/1VXJkZwZ", 
        caption="3 Pieces Art\nPrice: ETB 6000\nPhoto Code: 023",
        reply_markup=types.InlineKeyboardMarkup([
            [types.InlineKeyboardButton('🛒 Order Now', callback_data='order_Lior-WallArt-023')]
        ])
    )

    # Dog Sculpture
    bot.send_photo(
        message.chat.id, 
        "https://postimg.cc/s1g6Q580", 
        caption="Dog Sculpture\nPrice: ETB 2000\nPhoto Code: 024",
        reply_markup=types.InlineKeyboardMarkup([
            [types.InlineKeyboardButton('🛒 Order Now', callback_data='order_Lior-WallArt-024')]
        ])
    )

    # Cat Sculpture
    bot.send_photo(
        message.chat.id, 
        "https://postimg.cc/8sXyhjgk", 
        caption="Cat Sculpture\nPrice: ETB 2000\nPhoto Code: 025",
        reply_markup=types.InlineKeyboardMarkup([
            [types.InlineKeyboardButton('🛒 Order Now', callback_data='order_Lior-WallArt-025')]
        ])
    )

    # Wall Art (120*50cm)
    bot.send_photo(
        message.chat.id, 
        "https://postimg.cc/1V9hcPLR", 
        caption="Wall Art\nSize: 120*50cm\nPrice: ETB 8500\nPhoto Code: 026",
        reply_markup=types.InlineKeyboardMarkup([
            [types.InlineKeyboardButton('🛒 Order Now', callback_data='order_Lior-WallArt-026')]
        ])
    )

    # Bed Wall Art (2m*50cm)
    bot.send_photo(
        message.chat.id, 
        "https://postimg.cc/jCXrqw7D", 
        caption="Bed Wall Art\nSize: 2m*50cm\nPrice: ETB 7500\nPhoto Code: 027",
        reply_markup=types.InlineKeyboardMarkup([
            [types.InlineKeyboardButton('🛒 Order Now', callback_data='order_Lior-WallArt-027')]
        ])
    )

    # Leaves Wall Art
    bot.send_photo(
        message.chat.id, 
        "https://postimg.cc/tnRwnkxY", 
        caption="Leaves Wall Art\nHeight: 60cm\nPrice: ETB 4800\nPhoto Code: 028",
        reply_markup=types.InlineKeyboardMarkup([
            [types.InlineKeyboardButton('🛒 Order Now', callback_data='order_Lior-WallArt-028')]
        ])
    )

    # Frame Sculptures
    bot.send_photo(
        message.chat.id, 
        "https://postimg.cc/HczPmMhH", 
        caption="Frame Sculptures\nSize 30*30cm - ETB 1500\nSize 40*40cm - ETB 2000\nSize 50*50cm - ETB 2500\nPhoto Code: 029",
        reply_markup=types.InlineKeyboardMarkup([
            [types.InlineKeyboardButton('🛒 Order Now', callback_data='order_Lior-WallArt-029')]
        ])
    )

    # 3 Piece Frame Art
    bot.send_photo(
        message.chat.id, 
        "https://postimg.cc/HrMZxRh6", 
        caption="3 Piece Frame Art\nPrice: ETB 3000\nPhoto Code: 030",
        reply_markup=types.InlineKeyboardMarkup([
            [types.InlineKeyboardButton('🛒 Order Now', callback_data='order_Lior-WallArt-030')]
        ])
    )

    # 4 Piece Frame Art
    bot.send_photo(
        message.chat.id, 
        "https://postimg.cc/62WYM35P", 
        caption="4 Piece Frame Art\nPrice: ETB 3000\nPhoto Code: 031",
        reply_markup=types.InlineKeyboardMarkup([
            [types.InlineKeyboardButton('🛒 Order Now', callback_data='order_Lior-WallArt-031')]
        ])
    )

    # Parametric Frame Art (50*60cm)
    bot.send_photo(
        message.chat.id, 
        "https://postimg.cc/8sCZWjYJ", 
        caption="Parametric Frame Art\nSize: 50*60cm\nPrice: ETB 7500\nPhoto Code: 032",
        reply_markup=types.InlineKeyboardMarkup([
            [types.InlineKeyboardButton('🛒 Order Now', callback_data='order_Lior-WallArt-032')]
        ])
    )

    # Circular Blooming Sculptures (Golden-Silver)
    bot.send_photo(
        message.chat.id, 
        "https://postimg.cc/WhB8QS1g", 
        caption="Circular Blooming Sculptures (Golden-Silver)\n#1. 60-70 pieces: ETB 3800\n#2. 90-100 pieces: ETB 4500\n#3. 120-130 pieces: ETB 6000\nPhoto Code: 033",
        reply_markup=types.InlineKeyboardMarkup([
            [types.InlineKeyboardButton('🛒 Order Now', callback_data='order_Lior-WallArt-033')]
        ])
    )

    # Add the back button
    bot.send_message(message.chat.id, "Choose a category:", reply_markup=markup)#  
   
   # Function to handle the "Planters" button click
@bot.message_handler(func=lambda message: message.text == '🪴 Planters')
def show_planters(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    back_button = types.KeyboardButton('🔙 Back')
    markup.add(back_button)

    # Twisted Planter
    bot.send_photo(
        message.chat.id, 
        "https://postimg.cc/56ZnRTtZ", 
        caption="Twisted Planter\nPrice: ETB 800\nPhoto Code: 001",
        reply_markup=types.InlineKeyboardMarkup([
            [types.InlineKeyboardButton('🛒 Order Now', callback_data='order_Lior-Planter-001')]
        ])
    )

    # Cone Planter - Without Background
    bot.send_photo(
        message.chat.id, 
        "https://postimg.cc/nsxTHmB2", 
        caption="Cone Planter\nWithout Background\nPrice: ETB 600\nPhoto Code: 002",
        reply_markup=types.InlineKeyboardMarkup([
            [types.InlineKeyboardButton('🛒 Order Now', callback_data='order_Lior-Planter-002')]
        ])
    )

    # Cone Planter - With Background Plate
    bot.send_photo(
        message.chat.id, 
        "https://postimg.cc/18wJhBn4", 
        caption="Cone Planter\nWith Background Plate\nPrice: ETB 800\nPhoto Code: 003",
        reply_markup=types.InlineKeyboardMarkup([
            [types.InlineKeyboardButton('🛒 Order Now', callback_data='order_Lior-Planter-003')]
        ])
    )

    # Small Cactus Planter
    bot.send_photo(
        message.chat.id, 
        "https://postimg.cc/7GYVzyBT", 
        caption="Small Cactus Planter\nPrice: ETB 500\nPhoto Code: 004",
        reply_markup=types.InlineKeyboardMarkup([
            [types.InlineKeyboardButton('🛒 Order Now', callback_data='order_Lior-Planter-004')]
        ])
    )

    # Bigger Cactus Planter
    bot.send_photo(
        message.chat.id, 
        "https://postimg.cc/dZhjWjcs", 
        caption="Bigger Cactus Planter\nPrice: ETB 700\nPhoto Code: 005",
        reply_markup=types.InlineKeyboardMarkup([
            [types.InlineKeyboardButton('🛒 Order Now', callback_data='order_Lior-Planter-005')]
        ])
    )

    # Additional Small Planters
    bot.send_photo(
        message.chat.id, 
        "https://postimg.cc/SjRdNk2B", 
        caption="Planter\nPrice: ETB 500\nPhoto Code: 006",
        reply_markup=types.InlineKeyboardMarkup([
            [types.InlineKeyboardButton('🛒 Order Now', callback_data='order_Lior-Planter-006')]
        ])
    )

    bot.send_photo(
        message.chat.id, 
        "https://postimg.cc/vDKz4k5c", 
        caption="Planter\nPrice: ETB 700\nPhoto Code: 007",
        reply_markup=types.InlineKeyboardMarkup([
            [types.InlineKeyboardButton('🛒 Order Now', callback_data='order_Lior-Planter-007')]
        ])
    )

    bot.send_photo(
        message.chat.id, 
        "https://postimg.cc/3k5FBGSh", 
        caption="Planter\nPrice: ETB 400\nPhoto Code: 008",
        reply_markup=types.InlineKeyboardMarkup([
            [types.InlineKeyboardButton('🛒 Order Now', callback_data='order_Lior-Planter-008')]
        ])
    )

    bot.send_photo(
        message.chat.id, 
        "https://postimg.cc/mPYN6rJH", 
        caption="Planter (2 Pieces)\nPrice: ETB 600\nPhoto Code: 009",
        reply_markup=types.InlineKeyboardMarkup([
            [types.InlineKeyboardButton('🛒 Order Now', callback_data='order_Lior-Planter-009')]
        ])
    )

    bot.send_photo(
        message.chat.id, 
        "https://postimg.cc/t19t0jGm", 
        caption="Planter\nPrice: ETB 1500\nPhoto Code: 010",
        reply_markup=types.InlineKeyboardMarkup([
            [types.InlineKeyboardButton('🛒 Order Now', callback_data='order_Lior-Planter-010')]
        ])
    )

    # Wine Rack Designs
    bot.send_photo(
        message.chat.id, 
        "https://postimg.cc/0MBpJKML", 
        caption="Wine Rack Design\nSuitable for Kitchen & Dining Table\nPrice: ETB 2000\nPhoto Code: 011",
        reply_markup=types.InlineKeyboardMarkup([
            [types.InlineKeyboardButton('🛒 Order Now', callback_data='order_Lior-Planter-011')]
        ])
    )

    bot.send_photo(
        message.chat.id, 
        "https://postimg.cc/6y94fkS1", 
        caption="Wine Rack for 5 Bottles\nPrice: ETB 2000\nPhoto Code: 012",
        reply_markup=types.InlineKeyboardMarkup([
            [types.InlineKeyboardButton('🛒 Order Now', callback_data='order_Lior-Planter-012')]
        ])
    )

    bot.send_photo(
        message.chat.id, 
        "https://postimg.cc/NKnyY50W", 
        caption="Wine Cup Holder\nFor 3 Cups\nPrice: ETB 600\nPhoto Code: 013",
        reply_markup=types.InlineKeyboardMarkup([
            [types.InlineKeyboardButton('🛒 Order Now', callback_data='order_Lior-Planter-013')]
        ])
    )

    bot.send_message(message.chat.id, 'Select 🔙 Back to return to categories.', reply_markup=markup)
    # Function to handle the "Tables" button click
@bot.message_handler(func=lambda message: message.text == '🪑 Tables')
def show_tables(message):
    bot.send_message(
        message.chat.id, 
        "🪑 Our tables will be available soon! Thank you for your patience. 😊\n\n"
        "Meanwhile, feel free to explore our other amazing products:\n"
        "💡 Lights\n📚 Shelves\n🖼️ Wall Art & Sculptures\n🪴 Planters"
    )
    
# Function to handle the "Order Now" button click
@bot.callback_query_handler(func=lambda call: call.data.startswith('order_'))
def handle_order(call):
    product_code = call.data.split('_')[1]
    
    # Inform the user about the product and ask for customization
    bot.answer_callback_query(call.id, text=f'You selected {product_code}')
    
    # Ask for customization details
    bot.send_message(call.message.chat.id, f"Please write your order description and customization details for {product_code}. If there are no changes, type 'No customization'.")
    
    # Register the next step to capture customization details
    bot.register_next_step_handler(call.message, receive_customization, product_code)

# Function to receive customization details
def receive_customization(message, product_code):
    customization_text = message.text

    # Confirm or cancel order
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    confirm_button = types.KeyboardButton('✅ Confirm')
    cancel_button = types.KeyboardButton('❌ Cancel')
    markup.add(confirm_button, cancel_button)
    
    bot.send_message(
        message.chat.id,
        f"Order Details:\n\n"
        f"Product Code: {product_code}\n"
        f"Order Description and Customization: {customization_text}\n\n"
        "Do you confirm your order?",
        reply_markup=markup,
        parse_mode='Markdown'
    )

    # Register the next step for confirmation
    bot.register_next_step_handler(message, process_confirmation, product_code, customization_text)

# Function to process order confirmation
def process_confirmation(message, product_code, customization_text):
    if message.text == '✅ Confirm':
        order_message = (
    f"🛍️ New Order Received!\n\n"
    f"👤 Customer: {message.from_user.first_name} {message.from_user.last_name or ''}\n"
    f"📱 Username: @{message.from_user.username if message.from_user.username else 'N/A'}\n"
    f"🆔 User ID: {message.from_user.id}\n"
    f"📍 Chat ID: {message.chat.id}\n\n"
    f"🛒 Product Code: {product_code}\n"
    f"✏️ Order Description and Customization: {customization_text}\n"
    f"📅 Order Date: {message.date}\n"
    f"🚀 Status: Pending Confirmation\n\n"
    f"📩 Please contact the customer to confirm and arrange delivery."
)
        bot.send_message(SUPPORT_TEAM_CHAT_ID, order_message)
        bot.send_message(
            message.chat.id,
            "✅ Your order is confirmed! 📦\n"
            "Our support team will review your order and contact you soon.\n"
            "🔗 [Contact Support Team](https://t.me/Liordesign1)",
            parse_mode='Markdown'
        )
    elif message.text == '❌ Cancel':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        back_button = types.KeyboardButton('🔙 Back to Menu')
        markup.add(back_button)
        bot.send_message(message.chat.id, "❌ Your order has been canceled.", reply_markup=markup)

# Function to handle the "Back" button click
@bot.message_handler(func=lambda message: message.text == '🔙 Back')
def back(message):
    send_welcome(message)

# Function to handle the "Back to Menu" button click
@bot.message_handler(func=lambda message: message.text == '🔙 Back to Menu')
def back_to_menu(message):
    send_welcome(message)

# Polling the bot to keep it running
bot.polling(none_stop=True)
