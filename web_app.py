from flet import *

def main(page: Page):
    page.title = "Voltmart E-commerce website"
    page.bgcolor = colors.BLUE_600
    page.padding = 30  # 🔥 removes the top gap
    page.scroll = ScrollMode.ALWAYS
    # page.theme = ThemeMode.LIGHT
    

    logo = Image(
        src=r"assets\voltmart_logo.png",
        height= 55,
        width=280
    )

    def product_card(title, price, image):
        return Container(
            bgcolor= "white",
            padding= 20,
            border_radius= 12,
            content= Column(
                controls= [
                    Image(src=image, height= 150, width= 150, fit= ImageFit.CONTAIN),
                    Text(title, size= 18, weight= FontWeight.BOLD, color= "black"),
                    Text(f"₦{price}", size= 16, color= "green"),
                    ElevatedButton(
                        "Add to Cart", icon= icons.SHOPPING_CART
                    )                    
                ], horizontal_alignment= CrossAxisAlignment.CENTER
            ),
            col= {"sm": 12, "md": 4, "lg": 3}
        )

    appbar = AppBar(
        # leading= logo
        title= logo,
        actions=[
            TextButton(
                "HOME", on_click= lambda e: page.go("/")
            ),
            TextButton(
                "SHOP", on_click= lambda e: page.go("/shop")
            ),
            TextButton(
                "DEALS", on_click= lambda e: page.go("/deals")
            ),
            TextButton(
                "CART", on_click= lambda e: page.go("/cart")
            )
        ]
    )

    def route_change(route):
        page.views.clear()

        if page.route == "/":
            page.views.append(
                View(
                    "/",
                    scroll= ScrollMode.ALWAYS,
                    bgcolor= colors.BLUE_800,
                    controls= [
                        appbar,
                        Column(
               controls= [
                 Text(
                    "Welcome to Voltmart official website",
                    size= 30,
                    color= colors.WHITE70,
                    weight= FontWeight.BOLD
                ),
                Text(
                    "Smart Shopping starts here",
                    size= 25,
                    color= "white"
                ),
                Row(
                    controls= [
                        ElevatedButton(
                            text= "Start Shopping",
                            icon= icons.SHOPPING_CART,
                            on_click= lambda e: page.go("/shop")
                        ),
                        ElevatedButton(
                            text= "Explore Products",
                            icon= icons.EXPLORE_ROUNDED
                        ),
                    ],                    
                    alignment= MainAxisAlignment.SPACE_AROUND
                ),
                ResponsiveRow(
                    controls= [
                        Container(
                            content= Column(
                                controls=[
                                    Row(controls= [Text("⚡", size= 25,color= "yellow"), Text("Fast Delivery",size = 21,color= "blue")], spacing= 0.2),
                                    Text("Get your orders quickly and safely",size=17, color= "black")
                                ], spacing= 0.5
                            ), bgcolor= "white", padding= 40, border_radius= 20, col= {"sm": 12, "lg": 4, "md": 4}
                        ),

                        Container(
                            content= Column(
                                controls=[
                                    Row(controls= [Text("🔒", size= 25,color= "yellow"), Text("Secure Payments",size = 21,color= "blue")], spacing= 0.2),
                                    Text("Your transactions are always protected",size=17, color= "black")
                                ], spacing= 0.5
                            ), bgcolor= "white", padding= 40, border_radius= 20, col= {"sm": 12, "lg": 4, "md": 4}
                        ),

                        Container(
                            content= Column(
                                controls=[
                                    Row(controls= [Text("💯", size= 25,color= "yellow"), Text("Quality Product",size = 21,color= "blue")], spacing= 0.2),
                                    Text("Only Verified and Trusted Items",size=17, color= "black")
                                ], spacing= 0.5
                            ), bgcolor= "white", padding= 40, border_radius= 20, col= {"sm": 12, "lg": 4, "md": 4}
                        )

                    ],
                    alignment= MainAxisAlignment.SPACE_AROUND
                ), 

                Divider(height= 40, color= colors.WHITE24),
                Text(
                    "🔥 Featured Products",
                    size=28,
                    weight=FontWeight.BOLD,
                    color="white"
                ),
                ResponsiveRow(
                    controls=[
                        product_card("Iphone 17 Air", price= "1,300,000", image= r"assets\iphone17air.jpg"),
                        product_card("Iphone 17", price= "1,500,000", image= r"assets\iphone17basemodel.jpg"),
                        product_card("Iphone 17 pro Max", price= "1,900,000", image= r"assets\iphone17promax.jpg"),
                        product_card("Tecno Spark 40", price= "150,000", image= r"assets\tecnospark40.jpg"),
                        product_card("HP ELITEBOOK 840", price= "850,000", image= r"assets\laptop.webp"), 
                        product_card("Macbook M4 Air", price= "1,600,000", image= r"assets\macbookair.jpg"),
                        product_card("Oraimo Power Bank 8000mah", price= "28,356", image= r"assets\powerbank.jpg"),
                        product_card("Itel Power Station", price= "535,500", image= r"assets\itelpowerstation.webp"),
                    ]
                ),
                
                Text("Shop by Category", size= 24, weight= FontWeight.BOLD, color= "white"),
                ResponsiveRow(
                    alignment= MainAxisAlignment.SPACE_AROUND,
                    controls= [Container(
                        content= Row(
                            controls= [Text("Phone", size= 12, weight= FontWeight.BOLD, color= colors.CYAN_ACCENT_700)],
                        ),
                        padding= 12, border_radius= 17, bgcolor= "white", on_click= lambda e: page.go("/shop"),
                        col= {"sm": 6, "md": 3, "lg": 2}
                    ),
                    Container(
                        content= Row(
                            controls= [Text("Laptop", size= 12, weight= FontWeight.BOLD, color= colors.CYAN_ACCENT_700)],
                        ),
                        padding= 12, border_radius= 17, bgcolor= "white", on_click= lambda e: page.go("/shop"),
                        col= {"sm": 6, "md": 3, "lg": 2}
                    ),
                    Container(
                        content= Row(
                            controls= [Text("Phone and Laptop accessories", size= 12, weight= FontWeight.BOLD, color= colors.CYAN_ACCENT_700)],
                        ),
                        padding= 12, border_radius= 17, bgcolor= "white", on_click= lambda e: page.go("/shop"),
                        col= {"sm": 6, "md": 3, "lg": 2}
                    ),
                    Container(
                        content= Row(
                            controls= [Text("Others", size= 12, weight= FontWeight.BOLD, color= colors.CYAN_ACCENT_700)],
                        ),
                        padding= 12, border_radius= 17, bgcolor= "white", on_click= lambda e: page.go("/shop"),
                        col= {"sm": 6, "md": 3, "lg": 2}
                    )
                    ]
                ),
                Container(
                    padding= 25,
                    bgcolor= colors.BLUE_ACCENT_200,
                    border_radius= 18,
                    content= Row(
                        alignment= MainAxisAlignment.SPACE_BETWEEN,
                        controls= [
                         Column(
                            spacing= 6,
                            controls= [
                                Text("Flash Sale", weight= FontWeight.BOLD, size= 22, color= "white"),
                                Text("Up to 40% off on gadgets purchased today", size= 18, color= colors.WHITE70),
                                ElevatedButton(
                                    "Shop Deals",
                                    on_click= lambda e: page.go("/deals"),
                                    icon= icons.LOCAL_OFFER,
                                    bgcolor= colors.TEAL_ACCENT
                                )
                            ],
                         ), Icon(icons.FLASH_ON, size= 60, color= "Yellow")   
                        ]
                    )
                ),
                Divider(height=30, color=colors.WHITE24),

            Text("Top Brands", size=24, weight=FontWeight.BOLD, color="white"),

            Row(
                # scroll=ScrollMode.AUTO,
                alignment= MainAxisAlignment.SPACE_BETWEEN,
                controls=[
                    Container(bgcolor="black", padding=15, border_radius=15, content=Text("Apple", weight=FontWeight.BOLD, color= "white")),
                    Container(bgcolor="black", padding=15, border_radius=15, content=Text("Samsung", weight=FontWeight.BOLD, color= "white")),
                    Container(bgcolor="black", padding=15, border_radius=15, content=Text("HP", weight=FontWeight.BOLD, color= "white")),
                    Container(bgcolor="black", padding=15, border_radius=15, content=Text("Oraimo", weight=FontWeight.BOLD, color= "white")),
                    Container(bgcolor="black", padding=15, border_radius=15, content=Text("Tecno", weight=FontWeight.BOLD, color= "white")),
                ],
            ),
            Divider(height= 40, color= "white"),
            Text("What do our customers say?", size= 28, color= "white", weight= FontWeight.BOLD),
            ResponsiveRow(
                controls= [
                    Container(
                        bgcolor= "white",
                        padding= 20,
                        border_radius= 16,
                        content= Column(
                            controls= [
                                Row(controls= [Icon(icons.STAR, color= "amber"),Icon(icons.STAR, color= "amber"),Icon(icons.STAR, color= "amber"),Icon(icons.STAR, color= "amber")]),
                                Text("Delivery was fast and the product was legit", size = 20, color= "black"),
                                Text("-Mark Chukwueze", color= "black")
                            ]
                        ), col= {"sm": 12, "md": 6, "lg": 4}
                    ),

                    Container(
                        bgcolor= "white",
                        padding= 20,
                        border_radius= 16,
                        content= Column(
                            controls= [
                                Row(controls= [Icon(icons.STAR, color= "amber"),Icon(icons.STAR, color= "amber"),Icon(icons.STAR, color= "amber"),Icon(icons.STAR, color= "amber")]),
                                Text("My Goods came in faster than expected, great job guys!!", size = 20, color= "black"),
                                Text("-Ada Johnson", color= "black")
                            ]
                        ), col= {"sm": 12, "md": 6, "lg": 4}
                    ),

                    Container(
                        bgcolor= "white",
                        padding= 20,
                        border_radius= 16,
                        content= Column(
                            controls= [
                                Row(controls= [Icon(icons.STAR, color= "amber"),Icon(icons.STAR, color= "amber"),Icon(icons.STAR, color= "amber"),Icon(icons.STAR, color= "amber"),Icon(icons.STAR, color= "amber")]),
                                Text("Being using Voltmart for a while now they've never dissapointed", size = 20, color= "black"),
                                Text("-Heritage", color= "black")
                            ]
                        ), col= {"sm": 12, "md": 6, "lg": 4}
                    )
                ]
            )




               ], spacing= 30,
            )
                    ]
                )
            )

        elif page.route == "/shop":
            page.views.append(
                View(
                    "/shop",
                    bgcolor= colors.INDIGO_ACCENT_200,
                    scroll= ScrollMode.ALWAYS,
                    spacing= 15,
                    controls=[
                        appbar,
                        Text("Shop", size= 28, weight= FontWeight.BOLD),
                        Text("Browse and filter available products", color= colors.GREY_700),
                        TextField(
                            hint_text= "Search for a Product",
                            prefix_icon= icons.SEARCH,
                            border_radius= 16,
                            filled= True,
                            bgcolor= colors.GREY_700,
                            color="white"
                        ),
                        ResponsiveRow(
                            alignment= MainAxisAlignment.SPACE_AROUND,
                            controls= [
                                Dropdown(
                                autofocus= False,
                                bgcolor= "white",
                                border_radius= 16,
                                hint_text= "Select Category",
                                label= "Category", width= 200,
                                label_style= TextStyle(color= "white"),
                                text_style= TextStyle(color= "orange"),
                                options= [
                                    dropdown.Option("All"),
                                    dropdown.Option("Phones"),
                                    dropdown.Option("Laptops"),
                                    dropdown.Option("Accessories")
                                ], col= {"xs": 12, "sm": 6, "md": 6, "lg": 6}
                            ),

                            Dropdown(
                                label= "Sort by", hint_text= "Sort by",
                                label_style= TextStyle(color= "white"),
                                text_style= TextStyle(color= "orange"),
                                bgcolor= "orange",
                                width= 200,
                                options= [
                                    dropdown.Option("Newest"),
                                    dropdown.Option("Price: Low to High"),
                                    dropdown.Option("Price: High to Low")
                                ], border_radius= 16, col= {"xs": 12, "sm": 6, "md": 6, "lg": 6}
                            )
                            ]
                        ),
                        RadioGroup(
                            content= ResponsiveRow(
                                controls= [
                                    Radio(label= "All", value= "all", col= {"sm": 4, "xs": 4, "md": 4, "lg": 4}, fill_color= "white"),
                                    Radio(label= "Used", value= "used", col= {"sm": 4, "xs": 4, "md": 4, "lg": 4}, fill_color= "white"),
                                    Radio(label= "New", value= "new", col= {"sm": 4, "xs": 4, "md": 4, "lg": 4}, fill_color= "white")
                                ], 
                                alignment= MainAxisAlignment.SPACE_BETWEEN
                            )
                        ),
                        ResponsiveRow(
                            spacing= 14,
                            controls= [
                                TextField(
                                    label= "Min Price",
                                    border_radius= 14,
                                    prefix_text= "₦",
                                    width= 150,
                                    col= {"sm": 6, "xs": 6, "md": 6, "lg": 5}
                                ),
                                TextField(
                                    label= "Max Price",
                                    border_radius= 14,
                                    prefix_text= "₦",
                                    width= 150,
                                    col= {"sm": 6, "xs": 6, "md": 6, "lg": 5}
                                ),
                                ElevatedButton(
                                    text= "Apply",
                                    color= "white",
                                    bgcolor= "orange",
                                    icon= icons.FILTER_ALT,
                                    col= {"sm": 4, "xs": 4, "md": 6, "lg": 2},
                                    height=42
                                ),
                            ]
                        ),
                ResponsiveRow(
                    controls=[
                        product_card("Iphone 17 Air", price= "2,500,000", image= r"assets\iphone17air.jpg"),
                        product_card("Iphone 17 Pro", price= "2,590,000", image= r"assets\iphone17basemodel.jpg"),
                        product_card("Iphone 17 Pro Max", price= "2,700,000", image= r"assets\iphone17promax.jpg"),
                        product_card("Iphone 16", price= "1,860,000", image= r"assets\iphone16.jpg"),
                        product_card("Iphone 16 Pro", price= "1,920,000", image= r"assets\iphone16pro.jpg"),
                        product_card("Iphone 16 Pro Max", price= "2,100,000", image= r"assets\iphone16promax.jpg"),
                        product_card("Iphone 15", price= "1,600,000", image= r"assets\iphone15.jpg"),
                        product_card("Iphone 15 Pro", price= "1,738,000", image= r"assets\iphone15pro.jpg"),
                        product_card("Iphone 15 Pro Max", price= "1,738,000", image= r"assets\iphone15promax.jpg"),
                        product_card("Iphone 14", price= "850,900", image= r"assets\iphone14.jpg"),
                        product_card("Iphone 14 Pro", price= "850,900", image= r"assets\iphone14pro.jpg"),
                        product_card("Iphone 14 Pro Max", price= "850,900", image= r"assets\iphone14promax.jpg"),
                        product_card("Samsung S25 ULTRA", price= "1,400,000", image= r"assets\Samsung S25 Ultra.jpg"),
                        product_card("Samsung Z Flip", price= "2,205,000", image= r"assets\Samsung z flip.jpg"),
                        product_card("Iphone 14", price= "850,900", image= r"assets\iphone14.jpg"),
                        product_card("Tecno Spark 40", price= "150,000", image= r"assets\tecnospark40.jpg"),
                        product_card("HP ELITEBOOK 840", price= "850,000", image= r"assets\laptop.webp"), 
                        product_card("Macbook M4 Air", price= "1,600,000", image= r"assets\macbookair.jpg"),
                        product_card("Oraimo Power Bank 8000mah", price= "28,356", image= r"assets\powerbank.jpg"),
                        product_card("Itel Power Station", price= "535,500", image= r"assets\itelpowerstation.webp"),
                        
                    ]
                )
                    ],
                    padding=padding.all(50)
                )
            )

        elif page.route == "/deals":
            page.views.append(
                View(
                    "/deals",
                    bgcolor=colors.LIGHT_BLUE_100,
                    controls=[
                        appbar,
                        Column(
                            [
                                Text("Hot Deals 🔥", size=28, weight=FontWeight.BOLD),
                                ElevatedButton("Shop Deals", on_click=lambda e: page.go("/shop"))
                            ],
                            alignment=MainAxisAlignment.START,
                            horizontal_alignment=CrossAxisAlignment.CENTER,
                            spacing=15
                        )
                    ],
                    padding=padding.all(50)
                )
            )

        elif page.route == "/cart":
            page.views.append(
                View(
                    "/cart",
                    bgcolor=colors.LIGHT_GREEN_100,
                    controls=[
                        appbar,
                        Column(
                            [
                                Text("Your Cart", size=28, weight=FontWeight.BOLD),
                                ElevatedButton("Back to Home", on_click=lambda e: page.go("/"))
                            ],
                            alignment=MainAxisAlignment.START,
                            horizontal_alignment=CrossAxisAlignment.CENTER,
                            spacing=15
                        )
                    ],
                    padding=padding.all(50)
                )
            )
        page.update()


            

    
    
    # page.add(header)

    page.on_route_change = route_change
    page.go(page.route)

app(target=main, view=AppView.FLET_APP_WEB,assets_dir="assets")
