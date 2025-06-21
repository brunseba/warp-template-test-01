// MathJax configuration for Template Documentation

window.MathJax = {
  tex: {
    inlineMath: [["\\(", "\\)"]],
    displayMath: [["\\[", "\\]"]],
    processEscapes: true,
    processEnvironments: true,
    tags: 'ams',
    autoload: {
      color: [],
      colorV2: ['color']
    },
    packages: {'[+]': ['noerrors']}
  },
  chtml: {
    scale: 1.0,
    minScale: .5,
    matchFontHeight: false,
    displayAlign: 'center',
    displayIndent: '0em'
  },
  svg: {
    scale: 1.0,
    minScale: .5,
    matchFontHeight: false,
    displayAlign: 'center',
    displayIndent: '0em'
  },
  options: {
    ignoreHtmlClass: ".*|",
    processHtmlClass: "arithmatex"
  },
  loader: {
    load: ['[tex]/noerrors']
  }
};

document$.subscribe(() => {
  MathJax.typesetPromise()
});
