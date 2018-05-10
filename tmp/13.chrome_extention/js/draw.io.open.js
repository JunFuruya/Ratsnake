chrome.contextMenus.create({
    title: "draw.ioで開く",
    contexts: ["link"],
    onclick: function(info, tab) {
        var url = info.linkUrl;
        if (!url.match(/blob/)) return;
        if (!url.match(/\.xml$/)) return;
        url = url.replace("https://github.com/","");
        url = url.replace("blob/","");
        chrome.tabs.create({
            url: "https://www.draw.io/#H" + encodeURIComponent(url)
        });
    }
});
