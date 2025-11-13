# Solução para Erro de Instalação do Docker
## Erro: Wsl/CallMsi/Install/REGDB_E_CLASSNOTREG

Este erro ocorre durante a instalação do Docker Desktop no Windows quando há problemas com o WSL2 ou componentes do registro do Windows.

## Soluções (tente nesta ordem)

### Solução 1: Executar PowerShell como Administrador
1. Feche o instalador do Docker se estiver aberto
2. Clique com botão direito no menu Iniciar
3. Selecione "Windows PowerShell (Admin)" ou "Terminal (Admin)"
4. Execute novamente o instalador do Docker

### Solução 2: Reparar Componentes do Windows
Execute os seguintes comandos no PowerShell como Administrador:

```powershell
# Reparar componentes do sistema
DISM /Online /Cleanup-Image /RestoreHealth
sfc /scannow

# Reiniciar o computador após concluir
Restart-Computer
```

### Solução 3: Habilitar WSL2 Manualmente
Execute no PowerShell como Administrador:

```powershell
# Habilitar WSL
dism.exe /online /enable-feature /featurename:Microsoft-Windows-Subsystem-Linux /all /norestart

# Habilitar Plataforma de Máquina Virtual
dism.exe /online /enable-feature /featurename:VirtualMachinePlatform /all /norestart

# Reiniciar o computador
Restart-Computer
```

Após reiniciar:

```powershell
# Definir WSL2 como padrão
wsl --set-default-version 2

# Atualizar o kernel do WSL2
wsl --update
```

### Solução 4: Desinstalar e Reinstalar WSL
Se as soluções anteriores não funcionarem:

```powershell
# Desabilitar WSL
dism.exe /online /disable-feature /featurename:Microsoft-Windows-Subsystem-Linux

# Desabilitar Virtualização
dism.exe /online /disable-feature /featurename:VirtualMachinePlatform

# Reiniciar
Restart-Computer
```

Depois de reiniciar, execute novamente os comandos da Solução 3.

### Solução 5: Limpar Cache do Windows Installer
Execute no PowerShell como Administrador:

```powershell
# Parar o serviço Windows Installer
Stop-Service -Name msiserver -Force

# Limpar cache
Remove-Item -Path "$env:TEMP\*" -Recurse -Force -ErrorAction SilentlyContinue
Remove-Item -Path "C:\Windows\Installer\$patchcache$\*" -Recurse -Force -ErrorAction SilentlyContinue

# Reiniciar o serviço
Start-Service -Name msiserver
```

### Solução 6: Verificar e Reparar Registro do Windows
1. Pressione `Win + R`
2. Digite `regedit` e pressione Enter
3. Navegue até: `HKEY_CLASSES_ROOT\Installer`
4. Verifique se a chave existe
5. Se não existir, crie-a:
   - Clique com botão direito em `HKEY_CLASSES_ROOT`
   - Novo > Chave
   - Nome: `Installer`

### Solução 7: Baixar e Instalar Kernel WSL2 Manualmente
1. Baixe o kernel do WSL2:
   - [Download Kernel WSL2](https://wslstorestorage.blob.core.windows.net/wslblob/wsl_update_x64.msi)
2. Execute o instalador do kernel
3. Reinicie o computador
4. Tente instalar o Docker Desktop novamente

### Solução 8: Reinstalar Docker Desktop (Instalação Limpa)
```powershell
# Desinstalar Docker Desktop completamente
Get-Package "*Docker*" | Uninstall-Package

# Limpar pastas residuais
Remove-Item -Path "$env:APPDATA\Docker" -Recurse -Force -ErrorAction SilentlyContinue
Remove-Item -Path "$env:LOCALAPPDATA\Docker" -Recurse -Force -ErrorAction SilentlyContinue
Remove-Item -Path "$env:ProgramFiles\Docker" -Recurse -Force -ErrorAction SilentlyContinue

# Reiniciar
Restart-Computer
```

Depois de reiniciar:
1. Baixe a versão mais recente do Docker Desktop
2. Execute o instalador como Administrador
3. Marque a opção "Use WSL 2 instead of Hyper-V"

## Verificação Pós-Instalação

Após a instalação bem-sucedida, verifique:

```powershell
# Verificar versão do Docker
docker --version

# Verificar se o Docker está rodando
docker run hello-world

# Verificar WSL
wsl --list --verbose
```

## Requisitos do Sistema

Certifique-se de que seu sistema atende aos requisitos:
- Windows 10 versão 2004 ou superior (Build 19041+) ou Windows 11
- Virtualização habilitada na BIOS
- WSL 2
- Mínimo de 4GB de RAM (recomendado 8GB+)

## Links Úteis

- [Documentação Oficial Docker Desktop](https://docs.docker.com/desktop/install/windows-install/)
- [Documentação WSL2](https://docs.microsoft.com/en-us/windows/wsl/install)
- [Troubleshooting Docker Desktop](https://docs.docker.com/desktop/troubleshoot/overview/)

## Notas Importantes

- Sempre execute o PowerShell como Administrador
- Reinicie o computador após cada modificação significativa
- Desabilite temporariamente o antivírus se o problema persistir
- Verifique se a virtualização está habilitada na BIOS

---

**Status**: Se nenhuma dessas soluções funcionar, forneça mais detalhes sobre:
- Versão do Windows (execute `winver`)
- Logs completos do erro
- Resultado de `wsl --status`
