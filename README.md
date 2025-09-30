# Geld Maschine - Automatisches Online Einkommen Dashboard

A sophisticated web application for managing and monitoring automated online income streams in real-time. This dashboard provides comprehensive oversight of various financial metrics and facilitates interaction with different automated bots.

## 🚀 Features

- **Real-time Dashboard**: Live tracking of earnings, profits, and bot performance
- **Bot Management**: Control and monitor various automated income-generating bots
- **Interactive Charts**: Visual representation of daily earnings and performance metrics
- **Responsive Design**: Optimized for desktop, tablet, and mobile devices
- **Modern UI**: Built with React, Tailwind CSS, and shadcn/ui components

## 🤖 Supported Bot Types

- **Crypto Arbitrage Bot**: Automated cryptocurrency trading between exchanges
- **Forex Trading Bot**: AI-powered foreign exchange trading
- **Affiliate Marketing Bot**: Automated affiliate campaign management
- **Dropshipping Bot**: Product listing and order processing automation
- **Social Media Bot**: Automated content monetization
- **Mining Pool Bot**: Optimized crypto mining management

## 🛠️ Technology Stack

- **Frontend**: React 18 with Vite
- **Styling**: Tailwind CSS with shadcn/ui components
- **Charts**: Recharts for data visualization
- **Icons**: Lucide React icons
- **State Management**: React hooks (useState, useEffect)
- **Build Tool**: Vite
- **Package Manager**: pnpm

## 📦 Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd geld-maschine-frontend
   ```

2. Install dependencies:
   ```bash
   pnpm install
   ```

3. Start the development server:
   ```bash
   pnpm run dev
   ```

4. Open your browser and navigate to `http://localhost:5173`

## 🚀 Deployment

### Vercel Deployment

This project is optimized for deployment on Vercel:

1. Push your code to a GitHub repository
2. Connect your repository to Vercel
3. Vercel will automatically detect the Vite configuration and deploy

### Manual Build

To build for production:

```bash
pnpm run build
```

The built files will be in the `dist` directory.

## 📁 Project Structure

```
src/
├── components/
│   └── ui/          # shadcn/ui components
├── assets/          # Static assets
├── App.jsx          # Main application component
├── App.css          # Application styles
├── main.jsx         # Application entry point
└── index.css        # Global styles
```

## 🎨 Customization

The application uses Tailwind CSS for styling. You can customize:

- **Colors**: Modify the color scheme in `App.css`
- **Components**: Add new shadcn/ui components as needed
- **Layout**: Adjust the grid layouts and responsive breakpoints
- **Charts**: Customize chart appearance and data in the Recharts components

## 🔧 Development

### Available Scripts

- `pnpm run dev` - Start development server
- `pnpm run build` - Build for production
- `pnpm run preview` - Preview production build
- `pnpm run lint` - Run ESLint

### Adding New Features

1. **New Bot Types**: Add bot configurations to the `botData` array in `App.jsx`
2. **Additional Metrics**: Extend the metrics cards section
3. **New Charts**: Use Recharts components for additional visualizations
4. **API Integration**: Replace mock data with real API calls

## 🌟 Future Enhancements

- Backend API integration for real-time data
- User authentication and authorization
- Advanced analytics and reporting
- Mobile app development
- Multi-language support
- Dark/light theme toggle

## 📄 License

This project is licensed under the MIT License.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📞 Support

For support and questions, please open an issue in the GitHub repository.

---

**Note**: This is currently a frontend demonstration. For a fully functional application, backend services and API integrations are required as outlined in the project documentation.
