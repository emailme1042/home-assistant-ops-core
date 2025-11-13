# 📊 Dashboard Structure — Home Assistant UI Layout

## 🧭 Main Navigation Dashboards

### Primary Sidebar Entries
- **📊 SYSTEM_OVERVIEW** → `/system-overview/0`
  - Central system monitoring and AI work visibility
  - Anchored markdown content for session tracking
- **🤖 AI Navigation** → `/ai-navigation/ai-navigation`
  - Workflow guidance and session context
  - Links to session essentials and current work
- **🤖 AI Workspace** → `/ai-workspace/ai-overview`
  - Quick file access and validation tools
  - Script triggers and status monitoring

### User-Focused Dashboards
- **👤 User** → `/user-dash/0` — Personal control interface
- **👤 User Home** → `/user-dashboard/0` — Main user dashboard
- **🏠 (Default)** — Primary home control interface

### Operations Dashboards
- **📋 TODO & Next Actions** → `/ops-todo/0` — Task management
- **⚙️ Ops** → `/ops-dash/0` — Operational controls
- **🌐 Network** → `/network-diagnostics/0` — Network monitoring

## 🎛️ Admin & Management

### Admin Dashboard System
- **🔧 Admin** → `/admin-dash/0` — Main admin interface
- **🧩 Admin Batch 1-15** — Organized admin panels
  - Individual specialized control panels
  - Not shown in sidebar (accessed via main admin)
  - Covers different system aspects

### Specialized Control Panels
- **📺 Fire TV Remote** → `/fire-tv/0` — Media control
- **🧪 AI Sync Test** → `/test-sync/0` — Development testing

## 📁 Dashboard File Organization

### Core Structure
```
dashboards/
├── SYSTEM_OVERVIEW/           # System monitoring & AI work
│   ├── SYSTEM_OVERVIEW.yaml   # Main overview dashboard
│   ├── ai_navigation.yaml     # AI workflow navigation
│   └── [other overview files]
├── ai/                        # AI-specific dashboards
│   └── ai_workspace_overview.yaml
├── admin/                     # Administrative interfaces
│   ├── main_admin.yaml        # Primary admin dashboard
│   ├── admin_partials_batch1.yaml
│   ├── admin_partials_batch2.yaml
│   └── [batch3-15.yaml]       # Organized admin sections
├── ops/                       # Operational dashboards
│   ├── main.yaml              # Main ops dashboard
│   ├── todo-dashboard.yaml    # Task management
│   └── network_diagnostics.yaml
└── users/                     # User-focused interfaces
    ├── main.yaml              # Primary user dashboard
    ├── user_dashboard.yaml    # Personal interface
    └── fire_tv.yaml           # Media controls
```

### Dashboard Configuration Patterns
- **Mode**: All dashboards use `yaml` mode for version control
- **Icons**: Meaningful MDI icons for easy identification
- **Titles**: Clear, descriptive titles for navigation
- **Sidebar**: Strategic show/hide for clean navigation

## 🎯 AI Workspace Integration

### AI Navigation Dashboard
**Purpose**: Session workflow and context guidance
- Current session status and next steps
- Links to session essential files
- Quick access to AI protocols
- Multi-AI collaboration coordination

### AI Workspace Overview
**Purpose**: File access and validation tools  
- Direct file system integration
- Validation script triggers
- Status monitoring displays
- Development context access

### SYSTEM_OVERVIEW Dashboard
**Purpose**: Central monitoring and AI work visibility
- System health indicators
- Recent AI changes tracking  
- Validation results display
- Anchor points for all AI work

## 📱 Dashboard Features & Cards

### Common Card Types
- **Markdown Cards**: Rich content display, file links
- **Entities Cards**: Control and status display
- **Button Cards**: Action triggers and navigation
- **Auto-Entities**: Dynamic content generation
- **Custom Cards**: Enhanced functionality (HACS)

### Interactive Elements
- **Input Helpers**: User input collection
- **Validation Triggers**: One-click system checks
- **File Preview**: AI workspace file selection
- **Status Displays**: Real-time system monitoring

## 🔄 Dashboard Maintenance

### Update Patterns
- Modular YAML files for easy editing
- Include directives for shared components
- Version control friendly structure
- Systematic organization by function

### Content Management
- **Static Content**: Core dashboard structure
- **Dynamic Content**: Auto-entities for real-time data
- **AI-Generated**: Automated content from AI processes
- **User-Managed**: Personal preferences and settings

### Navigation Flow
1. **Entry Points**: Sidebar navigation to main dashboards
2. **Drill-Down**: Detailed views from overview dashboards
3. **Quick Actions**: Direct access to common functions
4. **Context Switching**: Easy movement between operational areas

## 🎨 Theming & Presentation

### Theme Support
- **Dynamic Themes**: User-selectable via `input_select.theme_mode`
- **Consistent Styling**: Shared theme across all dashboards
- **Accessibility**: Clear navigation and readable content

### Layout Principles
- **Information Hierarchy**: Most important items first
- **Logical Grouping**: Related functions together
- **Responsive Design**: Works on mobile and desktop
- **Minimal Clutter**: Focus on essential information

## 📊 Dashboard Performance

### Optimization Strategies
- **Lazy Loading**: Auto-entities only load when needed
- **Efficient Queries**: Minimal entity state polling
- **Cached Content**: Static content served efficiently
- **Progressive Enhancement**: Core functionality always available

### Health Monitoring
- Dashboard load times monitored
- Entity availability checking
- User interaction tracking
- Performance optimization ongoing

---

**Dashboard Count**: 15+ active dashboards  
**Navigation Type**: Hierarchical with quick access  
**Update Frequency**: As needed, version controlled  
**User Focus**: Balance between power and simplicity