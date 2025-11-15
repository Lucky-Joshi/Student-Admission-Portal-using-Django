# 🎨 UI Components Guide

## Available Components

### 1. Glass Cards

```html
<div class="glass-card p-8 rounded-3xl">
  <h3>Card Title</h3>
  <p>Card content</p>
</div>
```

**Features**: Frosted glass effect, backdrop blur, hover animation

### 2. Feature Cards

```html
<div class="feature-card">
  <div class="icon-wrapper">
    <i class="fas fa-icon"></i>
  </div>
  <h3>Feature Title</h3>
  <p>Description</p>
</div>
```

**Features**: Icon container, hover lift effect, smooth transitions

### 3. Primary Button

```html
<a href="#" class="btn-primary">
  Button Text <i class="fas fa-arrow-right ml-2"></i>
</a>
```

**Features**: Gradient background, shadow, hover lift

### 4. Secondary Button

```html
<a href="#" class="btn-secondary"> Button Text </a>
```

**Features**: Outlined style, hover fill effect

### 5. Floating Label Input

```html
<div class="floating-label-group">
  <input type="text" class="form-input" placeholder=" " required />
  <label>Label Text</label>
</div>
```

**Features**: Animated label, focus effects, validation states

### 6. Toast Notification

```javascript
showToast("Success message", "success");
showToast("Error message", "error");
```

**Features**: Auto-dismiss, slide-in animation, icon

### 7. Stat Card

```html
<div class="stat-card">
  <div class="text-5xl font-bold text-purple-600">500+</div>
  <div class="text-gray-600">Label</div>
</div>
```

**Features**: Counter animation, fade-in on scroll

### 8. Social Icons

```html
<a href="#" class="social-icon">
  <i class="fab fa-facebook-f"></i>
</a>
```

**Features**: Circular, hover effect, color transition

### 9. Animated Bubbles

```html
<div class="bubble bubble-1"></div>
<div class="bubble bubble-2"></div>
<div class="bubble bubble-3"></div>
```

**Features**: Rising animation, gradient background

### 10. Floating Element

```html
<div class="floating-element">
  <div class="glass-card">Content</div>
</div>
```

**Features**: Continuous float animation, parallax ready

## Color Classes (Tailwind)

### Text Colors

- `text-purple-600` - Primary purple
- `text-blue-600` - Secondary blue
- `text-pink-600` - Accent pink
- `text-gray-600` - Body text
- `text-gray-400` - Muted text

### Background Colors

- `bg-purple-600` - Primary background
- `bg-blue-600` - Secondary background
- `bg-white` - White background
- `bg-gray-900` - Dark background

### Gradient Backgrounds

```html
<div class="bg-gradient-to-r from-purple-600 to-blue-600">Gradient content</div>
```

## Animation Classes

### Fade In

```html
<div class="fade-in">Content</div>
```

### Floating

```html
<div class="floating-element">Content</div>
```

## Responsive Utilities

### Hide on Mobile

```html
<div class="hidden md:block">Desktop only</div>
```

### Show on Mobile

```html
<div class="md:hidden">Mobile only</div>
```

### Responsive Grid

```html
<div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
  <!-- Items -->
</div>
```

## JavaScript Functions

### Dark Mode Toggle

```javascript
// Automatically handled by main.js
// Toggle button: #darkModeToggle
```

### Show Toast

```javascript
showToast("Message", "success"); // or 'error'
```

### Smooth Scroll

```javascript
// Automatically applied to all anchor links
```

### Form Validation

```javascript
// Automatically applied to all forms
// Add 'required' attribute to inputs
```

## Icon Library (FontAwesome)

### Common Icons

- `fa-home` - Home
- `fa-user` - User
- `fa-envelope` - Email
- `fa-phone` - Phone
- `fa-check` - Check mark
- `fa-times` - Close
- `fa-arrow-right` - Arrow right
- `fa-bars` - Menu
- `fa-moon` - Moon (dark mode)
- `fa-sun` - Sun (light mode)

### Social Icons

- `fab fa-facebook-f`
- `fab fa-twitter`
- `fab fa-linkedin-in`
- `fab fa-instagram`
- `fab fa-github`

## Best Practices

1. **Always use semantic HTML**

   ```html
   <section>
     ,
     <article>
       ,
       <nav>
         ,
         <header>
           ,
           <footer></footer>
         </header>
       </nav>
     </article>
   </section>
   ```

2. **Add ARIA labels for accessibility**

   ```html
   <button aria-label="Close menu"></button>
   ```

3. **Use consistent spacing**

   - Small: `p-4` or `py-2 px-4`
   - Medium: `p-6` or `py-4 px-6`
   - Large: `p-8` or `py-6 px-8`

4. **Maintain color consistency**

   - Use defined color palette
   - Don't introduce random colors

5. **Test responsiveness**
   - Mobile: 375px, 414px
   - Tablet: 768px, 1024px
   - Desktop: 1280px, 1920px

## Example Page Structure

```html
{% extends 'app/base.html' %} {% block title %}Page Title{% endblock %} {% block
content %}
<section class="py-20 px-6">
  <div class="container mx-auto max-w-4xl">
    <h1 class="text-5xl font-bold text-center mb-12 fade-in">Page Heading</h1>

    <div class="glass-card p-8 rounded-3xl">
      <!-- Content -->
    </div>
  </div>
</section>
{% endblock %}
```

## Tips for Customization

1. **Change primary color**: Find/replace `#7c3aed` in CSS
2. **Adjust animations**: Modify keyframes in `style.css`
3. **Add new components**: Follow existing patterns
4. **Extend forms**: Use floating-label-group structure
5. **Add pages**: Copy existing template structure

Enjoy building beautiful UIs! 🎨
