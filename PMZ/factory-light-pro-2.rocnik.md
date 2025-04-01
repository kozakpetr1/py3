# Implementace systému zpráv

## Úloha 1: Objektové řešení

Vytvoř skript v Python, pro generování různých typů zpráv (`Message`) s využitím OOP a návrhového vroru Factory. 

### **Požadavky:**
1. **Vytvoř tovární třídu `MessageFactory`**, která na základě vstupních parametrů vrátí odpovídající instanci zprávy.
2. **Vytvoř třídu `Message`**, která bude mít metodu `get_content()`.
3. **Vytvoř konkrétní třídy** jako potomky třídy  `Message` pro různé typy zpráv:
   - `TextMessage` – SMS
   - `EmailMessage` – e-mail.
   - `PushNotification` – krátká notifikaci.
4. **Implementuj logiku vytváření zpráv.**
5. **Implementuj validaci vstupu – pokud se pokusíš vytvořit neznámý typ zprávy, program by měl vyvolat výjimku.**
6. **Metoda `get_content()` bude vrácet obsah zprávy ve formátu odpovídajícím danému typu zprávy.**
7. **Otestuj správnost implementace** voláním tovární metody a výpisem obsahu zpráv (`get_content()`). Příklady použítí a výpisu obsahu zpravy jsou uvedeny níže.


---

### **Příklad použití:**
```python
factory = MessageFactory()
message = factory.create_message("email")
print(message.get_content())
```

### **Příklad výpisu obsahu zprávy:**

#### **E-mailová zpráva**
```
From: odesilatel@example.com  
To: prijemce@example.com  
Subject: Předmět zprávy  

Dobrý den,  

toto je ukázkový text e-mailové zprávy.  

S pozdravem,  
[Vaše jméno]  
```

#### **Push notifikace**
Push notifikace se často posílají ve formátu JSON, například takto:
```json
{
    "title": "Nová zpráva",
    "message": "Máš novou notifikaci! Klikni pro více informací.",
    "timestamp": "2025-03-14T12:34:56Z"
}
```

#### **Text Message - základní formát SMS**
```
Odesílatel: +420123456789  
Příjemce: +420987654321  
Zpráva: Dobrý den, Vaše objednávka byla právě odeslána. Děkujeme za nákup!  
```