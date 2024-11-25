# Pixel & Paper

## About Pixel & Paper
Pixel & Paper is a digital marketplace for downloadable wall art. The platform offers a curated collection of high-quality digital prints that customers can instantly download and print at home or through their preferred printing service. With categories ranging from abstract art to typography and nature-inspired pieces, we provide beautiful, accessible art for every space.

## Screenshots
[Add actual screenshots of your deployed site here]

## Wireframes
![Desktop Homepage Wireframe](/workspace/wireframes/desktop-home.png)
![Mobile Product List Wireframe](/workspace/wireframes/mobile-products.png)
![Tablet Cart Wireframe](/workspace/wireframes/tablet-cart.png)

## User Stories
### As a Customer:
- I can browse through different categories of wall art so that I can find designs that match my style
- I can instantly download my purchased artwork so that I can print it immediately
- I can preview the artwork in detail before purchase so that I can make an informed decision
- I can create an account to save my favorite pieces and track my purchases
- I can add multiple items to my cart and checkout in one transaction
- I can see my order history and re-download past purchases

### As an Admin:
- I can add new artwork to the store so that I can expand the collection
- I can manage product categories and prices
- I can view customer orders and purchase history
- I can update product details and availability
- I can manage user accounts and permissions

## Design
The design emphasizes clean aesthetics and visual appeal, letting the artwork take center stage while maintaining intuitive navigation and seamless user experience.

### Colour Scheme
The site uses a sophisticated, neutral palette that complements the artwork:
- Primary: #333333 (Deep Charcoal)
- Secondary: #F5F5F5 (Light Gray)
- Accent: #4A90E2 (Ocean Blue)
- Text: #2C2C2C (Near Black)
- Background: #FFFFFF (White)

[Add color scheme image]

### Typography
- Headings: Cormorant Garamond - An elegant serif font that adds sophistication
- Body: Montserrat - A clean, modern sans-serif font for excellent readability
- Both fonts are from Google Fonts, ensuring consistent display across devices

## Features

### Current Features
- **Responsive Design**: Fully responsive across all devices
- **User Authentication**: Secure login and registration system
- **Shopping Cart**: Add multiple items and manage quantities
- **Secure Checkout**: Integration with Stripe for secure payments
- **Instant Downloads**: Automatic access to purchased files
- **Category Navigation**: Browse art by style and theme
- **Search Functionality**: Find specific artwork quickly
- **User Profiles**: Track orders and save favorites
- **Admin Dashboard**: Comprehensive product and order management

### Future Features
- **Artist Collaborations**: Platform for artists to sell their work
- **Custom Framing Options**: Integration with framing services
- **Room Visualization**: AR feature to preview art in your space
- **Print-on-Demand**: Direct integration with printing services
- **Gift Cards**: Digital gift card system
- **Subscription Service**: Monthly art downloads for subscribers

## Technologies Used
### Core Technologies
- **Django (5.1.3)**: Main framework
- **Python**: Backend programming
- **PostgreSQL**: Database management
- **AWS S3**: File storage for digital products
- **Stripe**: Payment processing

### Libraries & Frameworks
- **Django Allauth**: User authentication
- **Crispy Forms**: Form styling
- **Boto3**: AWS integration
- **Whitenoise**: Static file serving
- **Pillow**: Image processing
- **dj-database-url**: Database configuration

## Testing

### Automated Testing
- Unit tests for models and views
- Integration tests for payment processing
- Form validation testing
- URL routing tests

### Manual Testing
[Add detailed testing tables similar to Eco-Nomad format]

### Validator Testing
- HTML validation through W3C
- CSS validation through Jigsaw
- Python code linting through PEP8
- JavaScript validation through JSHint

### Device & Browser Testing
[Add compatibility tables similar to Eco-Nomad format]

## Deployment
### Heroku Deployment
[Add detailed deployment steps]

### Local Development
1. Clone the repository
2. Install dependencies
3. Set up environment variables
4. Configure AWS S3
5. Run migrations
6. Start the development server

## Credits
### Code
- Stripe integration based on Stripe's official documentation
- AWS S3 setup inspired by Django documentation

### Media
- Product images sourced from [list sources]
- Icons from FontAwesome

### Acknowledgments
- Code Institute for project structure guidance
- Mentor support and feedback
- Stack Overflow community for troubleshooting

## License
This project is licensed under the MIT License - see the LICENSE.md file for details