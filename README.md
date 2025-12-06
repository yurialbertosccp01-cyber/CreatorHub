# 🎬 Creator Hub

Uma plataforma moderna para criadores de conteúdo compartilharem e descobrirem filmes, séries, animes e jogos.

![Creator Hub](https://img.shields.io/badge/React-18.2.0-blue)
![Vite](https://img.shields.io/badge/Vite-4.4.5-green)
![License](https://img.shields.io/badge/License-MIT-yellow)

## 🌟 Funcionalidades

- ✅ **Sistema de Autenticação** - Login seguro com credenciais de teste
- ✅ **Navegação Intuitiva** - Seções organizadas para Filmes, Séries, Animes e Jogos
- ✅ **Sistema de Busca** - Busca inteligente por conteúdo
- ✅ **Publicação de Conteúdo** - Modal para criadores publicarem novo conteúdo
- ✅ **Interface Responsiva** - Design moderno e adaptável
- ✅ **Notificações** - Sistema de notificações integrado

## 🚀 Demo Online

**URL:** [Creator Hub Demo](https://work-1-mvuuuupskumwimgm.prod-runtime.all-hands.dev)

### 🔑 Credenciais de Teste:
- **Email:** teste@creatorhub.com
- **Senha:** 123456

## 📱 Como Executar no Android Studio

### Pré-requisitos

1. **Android Studio** (versão mais recente)
2. **Node.js** (versão 16 ou superior)
3. **Git** instalado

### 📋 Passo a Passo Completo

#### 1️⃣ **Clone o Repositório**

```bash
git clone https://github.com/yurialbertosccp01-cyber/CreatorHub.git
cd CreatorHub
```

#### 2️⃣ **Instale as Dependências**

```bash
npm install
```

#### 3️⃣ **Configure o Android Studio**

1. **Abra o Android Studio**
2. **Vá em File → Settings (ou Android Studio → Preferences no macOS)**
3. **Navegue até Tools → Terminal**
4. **Configure o Shell path para usar o terminal do sistema**

#### 4️⃣ **Abra o Projeto no Android Studio**

1. **File → Open**
2. **Selecione a pasta `CreatorHub`**
3. **Clique em OK**

#### 5️⃣ **Configure o Terminal Integrado**

1. **Abra o Terminal no Android Studio** (View → Tool Windows → Terminal)
2. **Navegue até a pasta do projeto:**
   ```bash
   cd CreatorHub
   ```

#### 6️⃣ **Execute o Projeto**

```bash
npm run dev
```

#### 7️⃣ **Acesse a Aplicação**

- **URL Local:** http://localhost:12000
- **URL de Rede:** http://[SEU_IP]:12000

### 🔧 **Configuração Avançada para Android Studio**

#### **Configurar Scripts no Android Studio:**

1. **Vá em Run → Edit Configurations**
2. **Clique no + e selecione "npm"**
3. **Configure os seguintes scripts:**

**Script de Desenvolvimento:**
- **Name:** Creator Hub - Dev
- **Command:** run
- **Scripts:** dev
- **Package.json:** [caminho para seu package.json]

**Script de Build:**
- **Name:** Creator Hub - Build
- **Command:** run
- **Scripts:** build
- **Package.json:** [caminho para seu package.json]

**Script de Preview:**
- **Name:** Creator Hub - Preview
- **Command:** run
- **Scripts:** preview
- **Package.json:** [caminho para seu package.json]

#### **Configurar Live Reload:**

1. **Instale a extensão "Live Edit" no Android Studio**
2. **O arquivo `vite.config.js` já está configurado para hot reload:**

```javascript
export default defineConfig({
  plugins: [react()],
  server: {
    host: '0.0.0.0',
    port: 12000,
    allowedHosts: [
      'work-1-mvuuuupskumwimgm.prod-runtime.all-hands.dev',
      'localhost',
      '127.0.0.1'
    ]
  }
})
```

### 🛠️ **Comandos Úteis**

```bash
# Instalar dependências
npm install

# Executar em modo desenvolvimento
npm run dev

# Fazer build para produção
npm run build

# Visualizar build de produção
npm run preview

# Verificar dependências desatualizadas
npm outdated

# Atualizar dependências
npm update
```

### 🐛 **Solução de Problemas Comuns**

#### **Erro de Porta em Uso:**
```bash
# Matar processo na porta 12000
npx kill-port 12000

# Ou usar porta diferente
npm run dev -- --port 3001
```

#### **Erro de Dependências:**
```bash
# Limpar cache e reinstalar
rm -rf node_modules package-lock.json
npm install
```

#### **Erro de Permissão (Linux/Mac):**
```bash
sudo chown -R $(whoami) ~/.npm
```

### 📱 **Testando no Dispositivo Móvel**

1. **Conecte seu dispositivo na mesma rede WiFi**
2. **Execute o projeto:**
   ```bash
   npm run dev
   ```
3. **Acesse pelo IP da máquina:**
   ```
   http://[SEU_IP]:12000
   ```

## 🚀 Versões Disponíveis

### 📱 Versão Web (React + Vite)
Aplicação web responsiva pronta para produção.

### 📱 Versão Mobile (React Native + Expo)
Aplicação mobile para Android e iOS.

## 🎨 Design

O aplicativo foi desenvolvido baseado no design fornecido, incluindo:
- Tela de login com autenticação social (Google, Apple) e email/senha
- Dashboard principal com navegação por categorias
- Modal de publicação de conteúdo
- Seção "Em Destaque" com carrossel de conteúdo
- Paleta de cores roxa/preta (#8B5CF6, #0a0a0a)

## 🛠️ Instalação e Execução

### Versão Web

```bash
# Navegar para o diretório raiz
cd CreatorHub

# Instalar dependências
npm install

# Executar em modo desenvolvimento
npm run dev

# Build para produção
npm run build
```

A aplicação estará disponível em `http://localhost:12000`

### Versão Mobile

```bash
# Navegar para o diretório mobile
cd CreatorHub/CreatorHubMobile

# Instalar dependências
npm install

# Instalar Expo CLI globalmente (se não tiver)
npm install -g @expo/cli

# Executar no simulador/dispositivo
expo start

# Para Android
expo start --android

# Para iOS
expo start --ios
```

## 📱 Funcionalidades Implementadas

### ✅ Versão Web
- [x] Tela de login com design idêntico ao mockup
- [x] Autenticação com Google, Apple e email/senha
- [x] Dashboard principal com navegação
- [x] Barra de busca funcional
- [x] Modal de publicação de conteúdo
- [x] Seção "Em Destaque" com carrossel
- [x] Sistema de roteamento
- [x] Design responsivo
- [x] Logout funcional

### ✅ Versão Mobile
- [x] Tela de login adaptada para mobile
- [x] Dashboard com navegação por abas
- [x] Modal de publicação responsivo
- [x] Lista horizontal de conteúdo em destaque
- [x] Navegação entre telas
- [x] Design otimizado para mobile
- [x] Suporte a iOS e Android

## 🎯 Para Publicação na Play Store

### Preparação do APK/AAB

1. **Configurar o projeto para produção:**
```bash
cd CreatorHubMobile
expo build:android
```

2. **Ou usar EAS Build (recomendado):**
```bash
# Instalar EAS CLI
npm install -g @expo/eas-cli

# Configurar build
eas build:configure

# Build para Android
eas build --platform android
```

3. **Gerar keystore para assinatura:**
```bash
# O Expo pode gerar automaticamente ou você pode usar sua própria keystore
eas build --platform android --clear-cache
```

### Configurações Necessárias

1. **Atualizar `app.json` com informações da Play Store:**
```json
{
  "expo": {
    "name": "Creator Hub",
    "android": {
      "package": "com.creatorhub.mobile",
      "versionCode": 1,
      "permissions": [],
      "icon": "./assets/icon.png",
      "adaptiveIcon": {
        "foregroundImage": "./assets/adaptive-icon.png",
        "backgroundColor": "#0a0a0a"
      }
    }
  }
}
```

2. **Criar ícones necessários:**
   - `assets/icon.png` (1024x1024)
   - `assets/adaptive-icon.png` (1024x1024)
   - `assets/splash.png` (1284x2778)

## 🔧 Tecnologias Utilizadas

### Web
- React 18.2.0
- Vite 4.4.5
- React Router DOM 6.8.1
- Lucide React (ícones)
- CSS3 com gradientes

### Mobile
- React Native 0.72.6
- Expo SDK 49
- React Navigation 6
- Expo Linear Gradient
- React Native Vector Icons

## 📁 Estrutura do Projeto

```
CreatorHub/
├── src/                    # Versão Web
│   ├── components/
│   │   ├── LoginPage.jsx
│   │   ├── Dashboard.jsx
│   │   └── PublishModal.jsx
│   ├── App.jsx
│   └── main.jsx
├── CreatorHubMobile/       # Versão Mobile
│   ├── screens/
│   │   ├── LoginScreen.js
│   │   └── DashboardScreen.js
│   ├── components/
│   │   └── PublishModal.js
│   ├── App.js
│   └── app.json
└── README.md
```

## 🎮 Como Testar

### Web
1. Execute `npm run dev`
2. Acesse `http://localhost:12000`
3. Teste o login com as credenciais: teste@creatorhub.com / 123456
4. Navegue pelo dashboard
5. Teste o modal de publicação
6. Teste o logout

### Mobile
1. Execute `expo start`
2. Use o Expo Go app no seu celular
3. Escaneie o QR code
4. Teste todas as funcionalidades

## 🚀 Deploy

### Web
```bash
# Build para produção
npm run build

# Deploy para Vercel, Netlify, ou qualquer hosting estático
```

### Mobile
```bash
# Build para Play Store
eas build --platform android --profile production

# Build para App Store
eas build --platform ios --profile production
```

## 📝 Próximos Passos

1. **Integração com Backend:**
   - API para autenticação real
   - Sistema de upload de arquivos
   - Banco de dados para conteúdo

2. **Funcionalidades Avançadas:**
   - Player de vídeo integrado
   - Sistema de comentários
   - Notificações push (mobile)
   - Modo offline

3. **Otimizações:**
   - Lazy loading de imagens
   - Cache de dados
   - Performance improvements

## 🤝 Contribuição

Este projeto foi desenvolvido seguindo exatamente o design fornecido nas imagens, com foco em:
- Fidelidade visual ao mockup
- Experiência de usuário otimizada
- Código limpo e bem estruturado
- Preparação para produção

---

**Desenvolvido com ❤️ usando React e React Native**