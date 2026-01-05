# 🔘 Zigbee Button Setup Guide

## 🎯 FIND YOUR BUTTON ENTITY

**Step 1: Identify Your Button**
1. Go to **Developer Tools → States**
2. Search for your button entity - likely one of:
   - `event.aqara_cube_always_add_via_server_not_here_button_5`
   - `event.aqara_cube_always_add_via_server_not_here_button_6` 
   - `button.0x00178801034dad85` (your recent Zigbee device)
   - Any entity containing "button" or starting with `event.`

**Step 2: Test Button Presses**
1. In **Developer Tools → Events**, listen for `state_changed` events
2. Press your physical button
3. Note the exact entity_id that appears

**Step 3: Update Automation**
Edit `includes/automations/zigbee_button_smart_downstairs.yaml` and replace:
```yaml
event_data:
  entity_id: event.aqara_cube_always_add_via_server_not_here_button_5
```
With your actual button entity.

## 🏠 DOWNSTAIRS DEVICES INCLUDED

### ✅ Lights (will turn off if ON):
- Hall light: `light.hallway_5` ← **Turns ON for 10 seconds**
- Lounge: `light.lounge`, `light.lounge_ceiling_light`, `light.lounge_light`
- Kitchen: `light.hue_kitchen`
- Dining: `light.dining_light_5`, `light.reading_light`, `light.brown_lamp`
- WiZ bulbs: `light.wiz_rgbw_tunable_2606be`, `light.wiz_rgbw_tunable_2609a6`
- Strip lights: `light.lounge_tv_strip_lights`

### 📺 Media Players (will turn off if PLAYING):
- **Apple TV SAFE**: Only turns off if actively playing
- Lounge: `media_player.lounge`
- Kitchen: `media_player.kitchen_nest`, `media_player.kitchen_alexa`
- Alexa: `media_player.lounge_alexa`

### 🔌 Switches (will turn off if ON):
- `switch.wax_warmer`
- `switch.lounge_loudness`
- `switch.lounge_speech_enhancement`

### 🪟 Covers (will close if OPEN):
- `cover.kitchen_blind`

## 🛡️ SAFETY FEATURES

✅ **No Apple TV Issues**: Only turns off if actively playing  
✅ **State Checking**: Only affects devices that are currently ON  
✅ **Continue on Error**: Won't stop if one device fails  
✅ **10 Second Timer**: Hall light stays on exactly 10 seconds  
✅ **Single Mode**: Prevents overlapping executions  

## 🚀 READY TO TEST

1. **Find your button entity** (Steps above)
2. **Update the automation** with correct entity
3. **Restart Home Assistant**
4. **Test the button** - Hall light should come on, downstairs devices turn off safely

**Expected Behavior:**
1. Press button → Hall light instantly ON (bright warm white)
2. All downstairs devices safely turn off (only if they were on)
3. After 10 seconds → Hall light turns off
4. Apple TV safe (only affects if actively playing)