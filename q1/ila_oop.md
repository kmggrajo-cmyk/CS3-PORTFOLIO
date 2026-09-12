# ILA 3-1: Applying the Four Pillars of OOP
## Sari-Sari Store Inventory System


### 1. Encapsulation
In designing a sari-sari store inventory system, encapsulation binds a product’s raw data and its operating methods inside a single class unit. The **Product** class groups internal fields like **name**, **price**, and **stockQuantity** alongside safe modifier methods such as **updateStock()**. Private access modifiers shield these sensitive price and inventory figures from unauthorized external modifications. Other parts of the program must interact with the data strictly through validated public functions. This protection prevents accidental data corruption and keeps the inventory state reliable during daily transactions.


### 2. Abstraction
Abstraction allows the sari‑sari store system to hide the complexity of its operations and present only the features that matter to clerks and customers. An abstract **BaseProduct** class defines essential required behaviors like **getDetails()** while leaving specific execution details to subclasses. For instance, a cashier can call **processSale(quantity)** or **getProductInfo()** without needing to understand how the program verifies stock, updates the database, or recalculates totals. This simplification reduces cognitive load when building the inventory dashboard and allows developers to modify low-level calculation rules later without breaking the user-facing interface modules. 


### 3. Inheritance
Inheritance lets specialized product types derive shared traits from a general parent class. A master **Product** class holds basic properties like **name** and **price**, which subclasses like **PerishableProduct**, **DiscountedProduct**, **FrozenProduct** automatically inherit. Instead of rewriting the stock tracking field for every new item type, the subclass reuses the parent structure entirely. Developers only write code for unique behaviors, such as adding an **expirationDate** property exclusively to perishable goods, **discountRate** to **DiscountedProduct**, or **storageTemp** to **FrozenProduct**. This hierarchical reuse mirrors how real stores categorize items, with perishable goods requiring expiration checks, discounted items needing price adjustments, and frozen products requiring precise storage temperature to preserve quality.


### 4. Polymorphism
Polymorphism lets different product classes share the same method name while executing distinct, type-specific actions. Both **PerishableProduct** and **DiscountedProduct** can implement a **calculateDiscount()** method, where one reduces prices near expiration and the other applies a flat percentage cut. The system processes these diverse items through a single interface, eliminating messy conditional chains. Developers can introduce new product variations later without altering the core processing loops. This design keeps the sari-sari store inventory system adaptable to future promotional rules with minimal code updates.

## Reflection
Among the four pillars of Object-Oriented Programming, encapsulation is the most valuable for improving the sari-sari store inventory system primarily because it locks raw item data inside a single class and controls how it changes. By making fields like **price** and **stockQuantity** private, the **Product** class blocks outside scripts from messing up numbers during fast sales. Any change to the count must go through safe functions like **updateStock()** that check if there is enough inventory left. This setup stops negative stock values or wrong pricing errors from breaking the store records. Ultimately, this data shielding keeps the daily inventory reliable and accurate.