document.addEventListener('DOMContentLoaded', function () {
    document.querySelectorAll('pre code').forEach((block) => {
        block.parentElement.classList.add('code-block');
        hljs.highlightBlock(block);
    });

    document.querySelectorAll('pre').forEach(function (pre) {
        var button = document.createElement('button');
        button.className = 'copy-button';
        button.textContent = 'Copy';
        pre.appendChild(button);
    });

    var clipboard = new ClipboardJS('.copy-button', {
        target: function(trigger) {
            return trigger.parentNode.querySelector('code');
        }
    });

    clipboard.on('success', function(e) {
        e.clearSelection();
        e.trigger.textContent = 'Copied!';
        setTimeout(function() {
            e.trigger.textContent = 'Copy';
        }, 2000);
    });

    clipboard.on('error', function(e) {
        e.trigger.textContent = 'Error!';
        setTimeout(function() {
            e.trigger.textContent = 'Copy';
        }, 2000);
    });
});
