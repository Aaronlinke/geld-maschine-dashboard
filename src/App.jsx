import { useState, useEffect } from 'react'
import { Button } from '@/components/ui/button.jsx'
import { Card, CardContent, CardHeader, CardTitle } from '@/components/ui/card.jsx'
import { Badge } from '@/components/ui/badge.jsx'
import { LineChart, Line, XAxis, YAxis, CartesianGrid, Tooltip, ResponsiveContainer } from 'recharts'
import { 
  TrendingUp, 
  Bot, 
  Target, 
  DollarSign, 
  Plus, 
  BarChart3, 
  Settings, 
  CreditCard,
  Bitcoin,
  TrendingDown,
  Link,
  Package,
  Smartphone,
  Pickaxe,
  Play,
  Pause,
  SettingsIcon
} from 'lucide-react'
import './App.css'

// Mock data for the daily earnings chart
const dailyEarningsData = [
  { time: '00:00', earnings: 0 },
  { time: '04:00', earnings: 8000 },
  { time: '08:00', earnings: 15000 },
  { time: '12:00', earnings: 28000 },
  { time: '16:00', earnings: 38000 },
  { time: '20:00', earnings: 45000 },
  { time: '24:00', earnings: 47523 }
]

// Mock bot data
const botData = [
  {
    id: 1,
    name: 'Crypto Arbitrage Bot',
    description: 'Automatischer Krypto-Handel zwischen Börsen',
    icon: Bitcoin,
    status: 'Aktiv',
    totalProfit: '€45,678.23',
    todayEarnings: '+€1,234.56',
    progress: 87,
    statusColor: 'bg-green-500'
  },
  {
    id: 2,
    name: 'Forex Trading Bot',
    description: 'KI-gestützter Devisenhandel',
    icon: TrendingUp,
    status: 'Aktiv',
    totalProfit: '€32,145.67',
    todayEarnings: '+€892.34',
    progress: 92,
    statusColor: 'bg-green-500'
  },
  {
    id: 3,
    name: 'Affiliate Marketing Bot',
    description: 'Automatische Affiliate-Kampagnen',
    icon: Link,
    status: 'Aktiv',
    totalProfit: '€18,934.21',
    todayEarnings: '+€456.78',
    progress: 76,
    statusColor: 'bg-green-500'
  },
  {
    id: 4,
    name: 'Dropshipping Bot',
    description: 'Produktlistung und Bestellabwicklung',
    icon: Package,
    status: 'Pausiert',
    totalProfit: '€28,567.89',
    todayEarnings: '+€723.45',
    progress: 45,
    statusColor: 'bg-yellow-500'
  },
  {
    id: 5,
    name: 'Social Media Bot',
    description: 'Automatisierte Content-Monetarisierung',
    icon: Smartphone,
    status: 'Aktiv',
    totalProfit: '€12,345.67',
    todayEarnings: '+€234.56',
    progress: 68,
    statusColor: 'bg-green-500'
  },
  {
    id: 6,
    name: 'Mining Pool Bot',
    description: 'Optimierte Krypto-Mining Verwaltung',
    icon: Pickaxe,
    status: 'Wartung',
    totalProfit: '€56,789.12',
    todayEarnings: '+€1,456.78',
    progress: 0,
    statusColor: 'bg-red-500'
  }
]

function App() {
  const [currentTime, setCurrentTime] = useState(new Date())

  useEffect(() => {
    const timer = setInterval(() => {
      setCurrentTime(new Date())
    }, 1000)

    return () => clearInterval(timer)
  }, [])

  const handleBotAction = (botId, action) => {
    console.log(`Bot ${botId}: ${action}`)
    // In a real app, this would make an API call
  }

  return (
    <div className="min-h-screen bg-gradient-to-br from-slate-900 via-slate-800 to-slate-900 text-white">
      {/* Header */}
      <header className="border-b border-slate-700 bg-slate-900/50 backdrop-blur-sm">
        <div className="container mx-auto px-6 py-4">
          <div className="flex items-center justify-between">
            <div>
              <h1 className="text-3xl font-bold bg-gradient-to-r from-green-400 to-emerald-500 bg-clip-text text-transparent">
                Geld Maschine Dashboard
              </h1>
              <p className="text-slate-400 mt-1">Automatische Einkommensströme in Echtzeit</p>
            </div>
            <div className="flex items-center gap-4">
              <Badge className="bg-green-500/20 text-green-400 border-green-500/30">
                🟢 Alle Systeme Online
              </Badge>
              <div className="text-right">
                <div className="text-3xl font-bold text-green-400">€47,523.84</div>
                <div className="text-sm text-slate-400">Heute verdient</div>
              </div>
            </div>
          </div>
        </div>
      </header>

      <div className="container mx-auto px-6 py-8">
        {/* Key Metrics */}
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6 mb-8">
          <Card className="bg-slate-800/50 border-slate-700 backdrop-blur-sm">
            <CardHeader className="flex flex-row items-center justify-between space-y-0 pb-2">
              <CardTitle className="text-sm font-medium text-slate-400">Gesamtgewinn</CardTitle>
              <DollarSign className="h-4 w-4 text-green-400" />
            </CardHeader>
            <CardContent>
              <div className="text-2xl font-bold text-white">€234,567.89</div>
              <p className="text-xs text-green-400 flex items-center gap-1">
                <TrendingUp className="h-3 w-3" />
                +12.5% vs. letzten Monat
              </p>
            </CardContent>
          </Card>

          <Card className="bg-slate-800/50 border-slate-700 backdrop-blur-sm">
            <CardHeader className="flex flex-row items-center justify-between space-y-0 pb-2">
              <CardTitle className="text-sm font-medium text-slate-400">Aktive Bots</CardTitle>
              <Bot className="h-4 w-4 text-blue-400" />
            </CardHeader>
            <CardContent>
              <div className="text-2xl font-bold text-white">8</div>
              <p className="text-xs text-green-400 flex items-center gap-1">
                <TrendingUp className="h-3 w-3" />
                +2 vs. letzten Monat
              </p>
            </CardContent>
          </Card>

          <Card className="bg-slate-800/50 border-slate-700 backdrop-blur-sm">
            <CardHeader className="flex flex-row items-center justify-between space-y-0 pb-2">
              <CardTitle className="text-sm font-medium text-slate-400">Erfolgsrate</CardTitle>
              <Target className="h-4 w-4 text-purple-400" />
            </CardHeader>
            <CardContent>
              <div className="text-2xl font-bold text-white">94.2%</div>
              <p className="text-xs text-green-400 flex items-center gap-1">
                <TrendingUp className="h-3 w-3" />
                +2.1% vs. letzten Monat
              </p>
            </CardContent>
          </Card>

          <Card className="bg-slate-800/50 border-slate-700 backdrop-blur-sm">
            <CardHeader className="flex flex-row items-center justify-between space-y-0 pb-2">
              <CardTitle className="text-sm font-medium text-slate-400">ROI (30 Tage)</CardTitle>
              <TrendingUp className="h-4 w-4 text-orange-400" />
            </CardHeader>
            <CardContent>
              <div className="text-2xl font-bold text-white">287%</div>
              <p className="text-xs text-green-400 flex items-center gap-1">
                <TrendingUp className="h-3 w-3" />
                +15.3% vs. letzten Monat
              </p>
            </CardContent>
          </Card>
        </div>

        <div className="grid grid-cols-1 lg:grid-cols-3 gap-8 mb-8">
          {/* Daily Earnings Chart */}
          <Card className="lg:col-span-2 bg-slate-800/50 border-slate-700 backdrop-blur-sm">
            <CardHeader>
              <CardTitle className="text-white">Tägliche Einnahmen in Echtzeit</CardTitle>
              <p className="text-slate-400 text-sm">Live-Tracking aller automatisierten Einkommensströme</p>
            </CardHeader>
            <CardContent>
              <ResponsiveContainer width="100%" height={300}>
                <LineChart data={dailyEarningsData}>
                  <CartesianGrid strokeDasharray="3 3" stroke="#374151" />
                  <XAxis dataKey="time" stroke="#9CA3AF" />
                  <YAxis stroke="#9CA3AF" />
                  <Tooltip 
                    contentStyle={{ 
                      backgroundColor: '#1F2937', 
                      border: '1px solid #374151',
                      borderRadius: '8px',
                      color: '#F9FAFB'
                    }} 
                  />
                  <Line 
                    type="monotone" 
                    dataKey="earnings" 
                    stroke="#10B981" 
                    strokeWidth={3}
                    dot={{ fill: '#10B981', strokeWidth: 2, r: 4 }}
                    activeDot={{ r: 6, stroke: '#10B981', strokeWidth: 2 }}
                  />
                </LineChart>
              </ResponsiveContainer>
            </CardContent>
          </Card>

          {/* Quick Actions */}
          <Card className="bg-slate-800/50 border-slate-700 backdrop-blur-sm">
            <CardHeader>
              <CardTitle className="text-white">Quick Actions</CardTitle>
            </CardHeader>
            <CardContent className="space-y-3">
              <Button className="w-full justify-start bg-green-600 hover:bg-green-700 text-white">
                <Plus className="mr-2 h-4 w-4" />
                Neuen Bot hinzufügen
              </Button>
              <Button className="w-full justify-start bg-blue-600 hover:bg-blue-700 text-white">
                <BarChart3 className="mr-2 h-4 w-4" />
                Detaillierte Analysen
              </Button>
              <Button className="w-full justify-start bg-orange-600 hover:bg-orange-700 text-white">
                <Settings className="mr-2 h-4 w-4" />
                System-Einstellungen
              </Button>
              <Button className="w-full justify-start bg-purple-600 hover:bg-purple-700 text-white">
                <CreditCard className="mr-2 h-4 w-4" />
                Auszahlung anfordern
              </Button>
            </CardContent>
          </Card>
        </div>

        {/* Active Bots */}
        <Card className="bg-slate-800/50 border-slate-700 backdrop-blur-sm">
          <CardHeader>
            <CardTitle className="text-white">Aktive Geld-Maschinen</CardTitle>
            <p className="text-slate-400 text-sm">Überwachen und verwalten Sie Ihre automatisierten Einkommensquellen</p>
          </CardHeader>
          <CardContent>
            <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
              {botData.map((bot) => {
                const IconComponent = bot.icon
                return (
                  <Card key={bot.id} className="bg-slate-700/50 border-slate-600 hover:bg-slate-700/70 transition-colors">
                    <CardHeader className="pb-3">
                      <div className="flex items-center justify-between">
                        <div className="flex items-center gap-3">
                          <div className="p-2 bg-slate-600 rounded-lg">
                            <IconComponent className="h-5 w-5 text-white" />
                          </div>
                          <div>
                            <h3 className="font-semibold text-white text-sm">{bot.name}</h3>
                            <p className="text-xs text-slate-400">{bot.description}</p>
                          </div>
                        </div>
                        <Badge className={`${bot.statusColor} text-white text-xs`}>
                          {bot.status}
                        </Badge>
                      </div>
                    </CardHeader>
                    <CardContent className="space-y-4">
                      <div className="grid grid-cols-2 gap-4 text-sm">
                        <div>
                          <p className="text-slate-400">Gesamtgewinn</p>
                          <p className="font-semibold text-white">{bot.totalProfit}</p>
                        </div>
                        <div>
                          <p className="text-slate-400">Heute</p>
                          <p className="font-semibold text-green-400">{bot.todayEarnings}</p>
                        </div>
                      </div>
                      
                      <div>
                        <div className="flex justify-between text-sm mb-1">
                          <span className="text-slate-400">Tagesfortschritt</span>
                          <span className="text-white">{bot.progress}%</span>
                        </div>
                        <div className="w-full bg-slate-600 rounded-full h-2">
                          <div 
                            className="bg-green-500 h-2 rounded-full transition-all duration-300" 
                            style={{ width: `${bot.progress}%` }}
                          ></div>
                        </div>
                      </div>

                      <div className="flex gap-2">
                        <Button 
                          size="sm" 
                          variant="outline" 
                          className="flex-1 border-slate-600 text-slate-300 hover:bg-slate-600"
                          onClick={() => handleBotAction(bot.id, 'settings')}
                        >
                          <SettingsIcon className="mr-1 h-3 w-3" />
                          Einstellungen
                        </Button>
                        <Button 
                          size="sm" 
                          className={`flex-1 ${
                            bot.status === 'Aktiv' 
                              ? 'bg-yellow-600 hover:bg-yellow-700' 
                              : 'bg-green-600 hover:bg-green-700'
                          }`}
                          onClick={() => handleBotAction(bot.id, bot.status === 'Aktiv' ? 'pause' : 'start')}
                        >
                          {bot.status === 'Aktiv' ? (
                            <>
                              <Pause className="mr-1 h-3 w-3" />
                              Pausieren
                            </>
                          ) : (
                            <>
                              <Play className="mr-1 h-3 w-3" />
                              Starten
                            </>
                          )}
                        </Button>
                      </div>
                    </CardContent>
                  </Card>
                )
              })}
            </div>
          </CardContent>
        </Card>
      </div>
    </div>
  )
}

export default App
