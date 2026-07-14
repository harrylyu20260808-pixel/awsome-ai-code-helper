# Deployment Guide

This guide covers how to deploy the AI Code Helper to various platforms.

本指南介绍如何将AI Code Helper部署到各种平台。

## GitHub Pages (Recommended)

### Automatic Deployment (CI/CD)

This project includes a GitHub Actions workflow that automatically deploys to GitHub Pages when you push to the `main` or `master` branch.

**Setup:**

1. Fork the repository
2. Enable GitHub Pages in repository settings:
   - Settings → Pages
   - Source: Select `gh-pages` branch
   - Save

3. Push your changes to `main` branch
4. GitHub Actions will automatically deploy to `https://yourusername.github.io/ai-code-helper/`

**Manual Deployment:**

```bash
# Build the project (no build process needed)
# Just ensure all files are present

# Push to main branch
git add .
git commit -m "Deploy to GitHub Pages"
git push origin main

# GitHub Actions will handle the deployment
```

### 部署到GitHub Pages（推荐）

### 自动部署（CI/CD）

本项目包含一个GitHub Actions工作流，当你推送到`main`或`master`分支时会自动部署到GitHub Pages。

**设置步骤：**

1. Fork仓库
2. 在仓库设置中启用GitHub Pages：
   - Settings → Pages
   - Source: 选择`gh-pages`分支
   - 保存

3. 将更改推送到`main`分支
4. GitHub Actions将自动部署到`https://yourusername.github.io/ai-code-helper/`

**手动部署：**

```bash
# 构建项目（无需构建过程）
# 确保所有文件存在即可

# 推送到main分支
git add .
git commit -m "Deploy to GitHub Pages"
git push origin main

# GitHub Actions将处理部署
```

## Traditional Static Hosting

### Netlify

1. Drag and drop the `english-prompt-library` folder to Netlify Drop
2. Or connect your GitHub repository
3. Site will be automatically deployed

### Netlify 部署

1. 将`english-prompt-library`文件夹拖放到Netlify Drop
2. 或连接你的GitHub仓库
3. 网站将自动部署

### Vercel

1. Import the project to Vercel
2. Configure build settings (no build needed)
3. Deploy

### Vercel 部署

1. 将项目导入Vercel
2. 配置构建设置（无需构建）
3. 部署

### Custom Web Server

For Apache:

```apache
<Directory "/path/to/english-prompt-library">
    Options Indexes FollowSymLinks
    AllowOverride None
    Require all granted

    # Ensure .html and .js files are served correctly
    AddDefaultCharset UTF-8
</Directory>
```

For Apache 部署

```apache
<Directory "/path/to/english-prompt-library">
    Options Indexes FollowSymLinks
    AllowOverride None
    Require all granted

    # 确保.html和.js文件正确提供
    AddDefaultCharset UTF-8
</Directory>
```

For Nginx:

```nginx
server {
    listen 80;
    server_name your-domain.com;

    root /path/to/english-prompt-library;
    index index.html;

    location / {
        try_files $uri $uri/ =404;
    }

    # Gzip compression
    gzip on;
    gzip_types text/plain text/css application/json application/javascript text/xml application/xml;

    # Cache static assets
    location ~* \.(js|css|png|jpg|jpeg|gif|ico|svg|woff|woff2|ttf|eot)$ {
        expires 1y;
        add_header Cache-Control "public, immutable";
    }
}
```

For Nginx 部署

```nginx
server {
    listen 80;
    server_name your-domain.com;

    root /path/to/english-prompt-library;
    index index.html;

    location / {
        try_files $uri $uri/ =404;
    }

    # Gzip压缩
    gzip on;
    gzip_types text/plain text/css application/json application/javascript text/xml application/xml;

    # 缓存静态资源
    location ~* \.(js|css|png|jpg|jpeg|gif|ico|svg|woff|woff2|ttf|eot)$ {
        expires 1y;
        add_header Cache-Control "public, immutable";
    }
}
```

## Local Development

To run locally:

```bash
# Navigate to the project directory
cd english-prompt-library

# Simply open index.html in a browser
# On macOS
open index.html

# On Windows
start index.html

# On Linux
xdg-open index.html
```

No server is required for development.

本地开发无需服务器。

## Performance Optimization

### Static Assets Caching

Add cache-control headers for static files in your web server configuration. This improves performance by serving cached versions of static files.

添加静态文件的缓存控制头以提高性能。通过提供缓存的静态文件版本，提升性能。

### Code Minification (Optional)

For production, you may want to minify HTML, CSS, and JavaScript:

```bash
# HTML minification (using clean-html-js)
npm install -g clean-html-js
clean-html-js index.html -o index.min.html

# CSS minification (using cssnano)
npm install -g cssnano-cli
cssnano style.css -o style.min.css

# JavaScript minification (using terser)
npm install -g terser
terser app.js -o app.min.js
```

Then update `index.html` to reference the minified versions.

然后更新`index.html`以引用最小化版本。

### Domain Setup

Add a `CNAME` file in the project root for custom domain:

在项目根目录添加`CNAME`文件以配置自定义域名：

```
yourdomain.com
```

## Monitoring and Analytics

### Analytics Tools

Consider adding analytics to track usage:

- Google Analytics 4
- Plausible (Privacy-friendly)
- Umami (Self-hosted)

### Analytics 工具

考虑添加分析工具以跟踪使用情况：

- Google Analytics 4
- Plausible（隐私友好）
- Umami（自托管）

## Troubleshooting

### 404 Errors

Ensure your web server is configured to serve `index.html` as the default file.

确保Web服务器配置为将`index.html`作为默认文件提供。

### JavaScript Not Loading

- Check browser console for errors
- Verify file paths in `index.html`
- Ensure `app.js` and `style.css` are in the same directory as `index.html`

### Stale Content

- Clear browser cache
- Verify files are up to date on the server
- Check for caching headers in server configuration

## Support

For deployment issues, please open an issue on GitHub.

如遇部署问题，请在GitHub上创建问题。

---

Happy deploying! 🚀
