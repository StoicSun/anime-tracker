## Stages of learning dearpygui

### Basic
- [x] Creating Widgets
- [x] Using Widgets
- [x] Widget Callbacks
- [x] Logging
- [x] Primary Window
- [x] Developer Tools

### Intermediate
- [x] Drawing API
- [x] Events, Inputs, and Item Polling
- [x] Runtime Adding and Deleting Widgets
- [x] Fonts and Unicode
- [x] Themes

### Advanced
- [ ] Values
- [x] Textures
- [ ] Child Operations, Slots
- [ ] Filter Set
- [x] Widget ID System
- [x] Item Configuration
- [ ] Parent Deduction & Container Stack
- [ ] Context Managers

### Widgets
- [x] Simple Plots
- [ ] Plots
- [ ] Table API
- [ ] File and Directory Selector
- [x] Menus
- [x] Tooltips
- [x] Popups
- [ ] Node Editor

## Some notes
- Unless an item is a root type or staging mode is active, all app items need to belong to a valid container item.
- All possible item config flags can be seen by doing the following:-  
`print(dpg.get_item_configuration(item))`