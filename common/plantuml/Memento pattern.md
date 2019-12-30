@startuml
skinparam classAttributeIconSize 0

package "class Memento(备忘录模式)" #DDDDDD {

    class Originator
    {
    +restore(Memento)
    +createMemento():Memento
    }
    note right: 负责创建备忘录

    class Memento
    {
    -mState
    +setState(int)
    +getState():int
    }
    note right: 备忘录

    class Caretaker
    {
    -mMemento:Memento
    +restoreMemento():Memento
    +storeMemento(Memento):void
    }
    note right:负责存储备忘录

    Originator ..> Memento
    Memento --o Caretaker
}
@enduml