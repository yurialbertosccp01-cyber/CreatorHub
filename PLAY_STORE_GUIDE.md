# 📱 Creator Hub - Guia Completo para Play Store

## 🎯 Status Atual

✅ **Aplicação Configurada e Pronta para Deploy**

- **Repositório**: https://github.com/yurialbertosccp01-cyber/CreatorHub.git
- **Projeto Mobile**: `/CreatorHubMobile/`
- **Package Name**: `com.creatorhub.mobile`
- **Version**: 1.0.0 (versionCode: 1)
- **Target SDK**: 34 (Android 14)

## 🚀 Como Gerar APK para Play Store

### Opção 1: EAS Build (Recomendado)

1. **Instalar EAS CLI**:
   ```bash
   npm install -g @expo/eas-cli
   ```

2. **Fazer login no Expo**:
   ```bash
   eas login
   ```

3. **Configurar projeto**:
   ```bash
   cd CreatorHubMobile
   eas build:configure
   ```

4. **Gerar APK para teste**:
   ```bash
   eas build --platform android --profile preview
   ```

5. **Gerar AAB para Play Store**:
   ```bash
   eas build --platform android --profile production
   ```

### Opção 2: Build Local com Expo

1. **Instalar dependências**:
   ```bash
   cd CreatorHubMobile
   npm install
   ```

2. **Gerar build**:
   ```bash
   npx expo build:android
   ```

### Opção 3: React Native CLI (Avançado)

1. **Ejetar do Expo** (se necessário):
   ```bash
   npx expo eject
   ```

2. **Build com Gradle**:
   ```bash
   cd android
   ./gradlew assembleRelease
   ```

## 📋 Checklist Pré-Deploy

### ✅ Configurações Obrigatórias

- [x] **Package Name**: `com.creatorhub.mobile`
- [x] **Version Code**: 1
- [x] **Target SDK**: 34
- [x] **Permissions**: INTERNET, ACCESS_NETWORK_STATE
- [x] **Icons**: Configurados (adaptive-icon.png)
- [x] **Splash Screen**: Configurado

### 🔧 Configurações Adicionais Necessárias

1. **Keystore para Assinatura**:
   ```bash
   keytool -genkey -v -keystore my-release-key.keystore -alias my-key-alias -keyalg RSA -keysize 2048 -validity 10000
   ```

2. **Configurar gradle.properties**:
   ```
   MYAPP_RELEASE_STORE_FILE=my-release-key.keystore
   MYAPP_RELEASE_KEY_ALIAS=my-key-alias
   MYAPP_RELEASE_STORE_PASSWORD=*****
   MYAPP_RELEASE_KEY_PASSWORD=*****
   ```

## 🎨 Assets Necessários

### Icons (Já configurados)
- **App Icon**: 1024x1024px
- **Adaptive Icon**: 432x432px
- **Splash Screen**: Configurado

### Screenshots para Play Store
Você precisará criar:
- **Phone**: 2-8 screenshots (16:9 ou 9:16)
- **Tablet**: 1-8 screenshots (opcional)
- **Feature Graphic**: 1024x500px

## 📝 Informações para Play Store

### Descrição do App
```
Creator Hub - Sua plataforma de entretenimento gratuita

Descubra filmes, séries, animes e jogos exclusivos em uma única plataforma. 
O Creator Hub oferece conteúdo de qualidade totalmente gratuito, com interface 
moderna e experiência otimizada para mobile.

Recursos:
• Catálogo diversificado de entretenimento
• Interface intuitiva e moderna
• Conteúdo gratuito e de qualidade
• Navegação por categorias
• Sistema de busca avançado
• Publicação de conteúdo pelos usuários

Baixe agora e explore um mundo de entretenimento!
```

### Categoria Sugerida
- **Entretenimento** ou **Mídia e Vídeo**

### Classificação Etária
- **Livre** (considerando o conteúdo atual)

## 🔧 Comandos Úteis

### Desenvolvimento
```bash
# Instalar dependências
npm install

# Iniciar em modo desenvolvimento
npx expo start

# Testar no Android
npx expo start --android

# Testar na web
npx expo start --web
```

### Build e Deploy
```bash
# Build para preview (APK)
eas build --platform android --profile preview

# Build para produção (AAB)
eas build --platform android --profile production

# Verificar status do build
eas build:list

# Submit para Play Store
eas submit --platform android
```

## 🐛 Troubleshooting

### Problemas Comuns

1. **Erro de dependências**:
   ```bash
   npx expo install --fix
   ```

2. **Problemas de build**:
   ```bash
   npx expo doctor
   ```

3. **Limpar cache**:
   ```bash
   npx expo start --clear
   ```

## 📱 Testando o App

### No Dispositivo Físico
1. Instale o **Expo Go** da Play Store
2. Execute `npx expo start`
3. Escaneie o QR code com o Expo Go

### No Emulador
1. Configure Android Studio
2. Execute `npx expo start --android`

## 🎯 Próximos Passos

1. **Gerar APK de teste** com EAS Build
2. **Testar em dispositivos reais**
3. **Criar assets para Play Store** (screenshots, etc.)
4. **Configurar keystore** para assinatura
5. **Fazer upload na Play Console**
6. **Configurar listing** na Play Store
7. **Submeter para revisão**

## 📞 Suporte

- **Expo Documentation**: https://docs.expo.dev/
- **React Native Guide**: https://reactnative.dev/docs/signed-apk-android
- **Play Console Help**: https://support.google.com/googleplay/android-developer/

---

**🎉 Seu app está pronto para a Play Store!**

Execute os comandos acima para gerar o APK/AAB e fazer o upload na Google Play Console.