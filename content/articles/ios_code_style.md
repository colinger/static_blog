Title: iOS编码规范参考
Date: 2014-12-24 02:06
Category: iOS
Tags: iOS
Slug: iso-code-style
Author: Colin
Summary: 编码规范对于程序员而言尤为重要，有以下几个原因：一个软件的生命周期中，80%的花费在于维护；几乎没有任何一个软件，在其整个生命周期中，均由最初的开发人员来维护；编码规范可以改善软件的可读性，可以让程序员尽快而彻底地理解新的代码；如果你将源码作为产品发布，就需要确任它是否被很好的打包并且清晰无误，一如你已构建的其它任何产品

##注释

建议使用[VVDocumenter](https://github.com/onevcat/VVDocumenter-Xcode)插件 

###多行注释
####格式
```
/**

              注释内容
*/
```
###单行注释
####格式
```
///在对文件、类、函数进行注释时推荐使用多行注释，在函数体内对代码块进行注释时，使用单行注释
```
###函数的注释

####函数注释的格式为
```
/**
 *  @brief  
 *  @param
 *  @return
 **/
 在brief中需要写明函数的主要功能、注意事项
 在param中需要写明函数的变量类型、变量的作用
 在return中需要写明函数的返回类型、返回值的作用
 如有其他需要说明的地方，可以在@return后面添加新项。如
 /**
 *  @brief  
 *  @param
 *  @return
 *  @warning
 **/

/**
 *  @brief      上传图片。上传成功后会自动将图片放入缓存，缓存的key为图片的url
 *  @param      UIImage，需要上传的图片
 *  @return     void
 *  @blocks
 *              success:返回的NSDictionary中包含服务器的response信息，包括图片id（id）,url(url),宽度(width),高度(height)。使用括号中的名称从NSDictionary中获取。
 *              failed:返回error
 **/
```