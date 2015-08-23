Title: 无线分发应用--通过Safari安装App 
Date: 2015-01-21 21:20
Category: iOS
Tags: iOS, util, base64
Slug: ios-dispatch-safari



### iOS 支持以无线方式安装企业级应用程序，这可让您在不使用 iTunes 的情况下将内部软件分发给用户。

###简单几步：

用户需要将设备的UDID加到 Apple Developer Center 中心的设备里，并更新 .mobileprovision文件

Scheme 里将 Archive 的 Build Configuration 换成 Debug 模式

Archive 后从 Organizer 找到app文件，生成 ipa 文件

生成 plist 文件，将它与 ipa 文件放到服务器上，并可通过网址访问并可下载

做一个网页供大家访问后点键接跳转下载此plist, 如果生成将网址生成一个二维码，就更方便了。

比如:
```
<a href="itms-services://?action=download-manifest&url=http://example.com/manifest.plist">Install App</a>
```
####plist 文件模板:

>    注: {}里的内容是要替换的

```
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>items</key>
    <array>
        <dict>
            <key>assets</key>
            <array>
                <dict>
                    <key>kind</key>
                    <string>software-package</string>
                    <key>url</key>
                    <string>{你的域名http://doruby.com/xxx.ipa}</string>
                </dict>
            </array>
            <key>metadata</key>
            <dict>
                <key>bundle-identifier</key>
                <string>{你的bundle identifier}</string>
                <key>bundle-version</key>
                <string>1.0</string>
                <key>kind</key>
                <string>software</string>
                <key>title</key>
                <string>{App名称}</string>
            </dict>
        </dict>
    </array>
</dict>
</plist>
```

### 网页模板

>    注: {}里的内容是要替换的

```
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
<meta name="viewport" content="width=320, height=460, user-scalable=no,
initial-scale=1.0" />
<title>Install Dev App</title>
</head>
<br/><br/><br/>
<body>
<div align="center">
<a href="itms-services://?action=download-manifest&url={http://doruby.com/xxx.plist}"  style="color:orange; font-size:24px">Install the App</a>
</div>
</body>
</html>
```

注意:

可能需要配置你的 Web 服务器以便正确地传输清单文件和应用程序文件。

对于 OS X Server，将以下 MIME 类型添加到 Web 服务的“MIME Types”（MIME 类型）设置中：
application/octet-stream ipa
text/xml plist

对于 IIS，使用 IIS Manager 在服务器的“属性”页面中添加 MIME 类型：
.ipa application/octet-stream
.plist text/xml

>
iOS 7.1修改了manifest.plist文件的访问协议，之前可以通过http协议访问，在iOS 7.1之后必须使用https协议方式访问。
>
比如之前的链接代码为：
>
itms-services://?action=download-manifest&url=http://doruby.com/manifest.plist

需要修改为：
>
itms-services://?action=download-manifest&url=https://doruby.com/manifest.plist

如果你没有放置或制作 SSL 证书的地方，可以将 plist 文件放到 Dropbox 上，然后得到文件的下载地址： 
>https://www.dropbox.com/s/s3zl5vzxgvjtwfw/app.plist, 替换 www.dropbox.com 为 dl.dropboxusercontent.com 即可。
