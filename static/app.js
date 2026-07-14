// Tab Navigation
document.addEventListener('DOMContentLoaded', function() {
    const tabBtns = document.querySelectorAll('.tab-btn');
    const tabContents = document.querySelectorAll('.tab-content');

    tabBtns.forEach(btn => {
        btn.addEventListener('click', function() {
            // Remove active class from all buttons
            tabBtns.forEach(b => b.classList.remove('active'));
            // Remove active class from all contents
            tabContents.forEach(c => c.classList.add('hidden'));

            // Add active class to clicked button
            this.classList.add('active');

            // Show corresponding content
            const tabName = this.getAttribute('data-tab');
            const targetTab = document.getElementById(tabName + '-tab');
            if (targetTab) {
                targetTab.classList.remove('hidden');
            }
        });
    });
});

// Generate Code
document.getElementById('generate-btn').addEventListener('click', async function() {
    const requirement = document.getElementById('requirement').value.trim();
    const language = document.getElementById('language').value;

    if (!requirement) {
        alert('请输入你的需求！');
        return;
    }

    const btn = this;
    btn.textContent = '⏳ 生成中...';
    btn.disabled = true;

    try {
        const response = await fetch('/api/generate-code', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                requirement: requirement,
                language: language
            })
        });

        const data = await response.json();

        document.getElementById('code-content').textContent = data.code;
        document.getElementById('generated-code').textContent = data.code;
        document.getElementById('explanation-text').textContent = data.explanation;
        document.getElementById('explanation-text').classList.remove('hidden');
        document.getElementById('result-area').classList.remove('hidden');

    } catch (error) {
        alert('生成代码失败，请检查网络连接！');
        console.error('Error:', error);
    } finally {
        btn.textContent = '✨ 生成代码';
        btn.disabled = false;
    }
});

// Debug Code
document.getElementById('debug-btn').addEventListener('click', async function() {
    const error = document.getElementById('error').value.trim();
    const code = document.getElementById('debug-code').value.trim();

    if (!error || !code) {
        alert('请输入报错信息和代码！');
        return;
    }

    const btn = this;
    btn.textContent = '⏳ 修复中...';
    btn.disabled = true;

    try {
        const response = await fetch('/api/debug-code', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                error: error,
                code: code
            })
        });

        const data = await response.json();

        document.getElementById('error-analysis').innerHTML = data.analysis;
        document.getElementById('debug-code-content').textContent = data.fixed_code;
        document.getElementById('fixed-code').textContent = data.fixed_code;
        document.getElementById('debug-result').classList.remove('hidden');

    } catch (error) {
        alert('修复代码失败，请检查网络连接！');
        console.error('Error:', error);
    } finally {
        btn.textContent = '🔧 自动修复';
        btn.disabled = false;
    }
});

// Check if page loaded with initial code (from URL parameter)
const urlParams = new URLSearchParams(window.location.search);
const initialCode = urlParams.get('code');

if (initialCode) {
    document.getElementById('explain-code').value = decodeURIComponent(initialCode);
}

// Explain Line
document.getElementById('explain-btn').addEventListener('click', async function() {
    const code = document.getElementById('explain-code').value.trim();
    const lineNumber = parseInt(document.getElementById('line-number').value);

    if (!code) {
        alert('请输入代码！');
        return;
    }

    const btn = this;
    btn.textContent = '⏳ 解释中...';
    btn.disabled = true;

    try {
        const response = await fetch('/api/explain-line', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                code: code,
                line_number: lineNumber
            })
        });

        const data = await response.json();

        document.getElementById('explanation-content').innerHTML = data.explanation;
        document.getElementById('explain-result').classList.remove('hidden');

    } catch (error) {
        alert('代码解释失败，请检查网络连接！');
        console.error('Error:', error);
    } finally {
        btn.textContent = '📚 开始解释';
        btn.disabled = false;
    }
});

// Copy Code
document.getElementById('copy-btn').addEventListener('click', async function() {
    const code = document.getElementById('code-content').textContent;

    try {
        await navigator.clipboard.writeText(code);
        const originalText = this.textContent;
        this.textContent = '✅ 已复制！';
        setTimeout(() => {
            this.textContent = originalText;
        }, 2000);
    } catch (error) {
        alert('复制失败，请手动复制！');
        console.error('Error:', error);
    }
});

// Download Code
document.getElementById('download-btn').addEventListener('click', async function() {
    const language = document.getElementById('language').value;
    const code = document.getElementById('code-content').textContent;

    // Determine file extension
    let extension = 'py';
    if (language === 'JavaScript') extension = 'js';
    if (language === 'Java') extension = 'java';
    if (language === 'C++') extension = 'cpp';

    const filename = `generated_code.${extension}`;

    try {
        const blob = new Blob([code], { type: 'text/plain' });
        const url = URL.createObjectURL(blob);
        const a = document.createElement('a');
        a.href = url;
        a.download = filename;
        document.body.appendChild(a);
        a.click();
        document.body.removeChild(a);
        URL.revokeObjectURL(url);
    } catch (error) {
        alert('下载失败，请手动保存！');
        console.error('Error:', error);
    }
});

// Debug Copy Code
document.getElementById('debug-copy-btn').addEventListener('click', async function() {
    const code = document.getElementById('debug-code-content').textContent;

    try {
        await navigator.clipboard.writeText(code);
        const originalText = this.textContent;
        this.textContent = '✅ 已复制！';
        setTimeout(() => {
            this.textContent = originalText;
        }, 2000);
    } catch (error) {
        alert('复制失败，请手动复制！');
        console.error('Error:', error);
    }
});

// Debug Download Code
document.getElementById('debug-download-btn').addEventListener('click', async function() {
    const code = document.getElementById('debug-code-content').textContent;
    const language = document.getElementById('language').value || 'Python';

    let extension = 'py';
    if (language === 'JavaScript') extension = 'js';
    if (language === 'Java') extension = 'java';
    if (language === 'C++') extension = 'cpp';

    const filename = `fixed_code.${extension}`;

    try {
        const blob = new Blob([code], { type: 'text/plain' });
        const url = URL.createObjectURL(blob);
        const a = document.createElement('a');
        a.href = url;
        a.download = filename;
        document.body.appendChild(a);
        a.click();
        document.body.removeChild(a);
        URL.revokeObjectURL(url);
    } catch (error) {
        alert('下载失败，请手动保存！');
        console.error('Error:', error);
    }
});
