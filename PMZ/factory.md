# Implementace systému zpráv

## Úloha 1: Objektové řešení

Vytvoř skript (PHP, Python, node.js) pro generování různých typů zpráv (`Message`) s využitím OOP. 

### **Požadavky:**
1. **Vytvoř abstraktní třídu `Message`**, která bude mít metodu `get_content()`.
2. **Vytvoř konkrétní třídy** pro různé typy zpráv:
   - `TextMessage` – vrací textový obsah.
   - `EmailMessage` – obsahuje předmět a tělo emailu.
   - `PushNotification` – obsahuje krátkou notifikaci.
3. **Implementuj logiku vytváření zpráv přímo ve svém hlavním programu.**
4. **Metoda `get_content()` bude vrácet pouze typ zprávy.**
5. **Otestuj svou implementaci** voláním jednotlivých tříd a výpisem typu zprávy (`get_content()`).

---

## **Úloha 2: Implementace s návrhovým vzorem Factory**

Přepracuj svou implementaci tak, aby využívala návrhový vzor Factory.

#### **Požadavky:**
1. **Vytvoř tovární třídu `MessageFactory`**, která na základě vstupních parametrů vrátí odpovídající instanci zprávy.
2. **Refaktoruj svůj kód tak, aby vytvoření objektů probíhalo přes tovární metodu místo přímého volání konstruktorů jednotlivých tříd.**
3. **Implementuj validaci vstupu – pokud se pokusíš vytvořit neznámý typ zprávy, program by měl vyvolat výjimku.**
4. **Metoda `get_content()` bude vrácet obsah zprávy ve formátu odpovídajícím danému typu zprávy.**
5. **Otestuj správnost implementace** voláním tovární metody a výpisem obsahu zpráv (`get_content()`).

---

### **Příklad použití (pro druhou část – s Factory patternem):**
```python
factory = MessageFactory()
message = factory.create_message("email")
print(message.get_content())
```

```php
$factory = new MessageFactory();
$message = $factory->createMessage("push");
echo $message->getContent();
```

```javascript
const factory = new MessageFactory();
const message = factory.createMessage("text");
console.log(message.getContent());
```
### **Příklad výsipu obsahu zprávy pro úlohu 2**

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