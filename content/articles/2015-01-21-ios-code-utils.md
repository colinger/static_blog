Title: iOS代码小贴士-001
Date: 2015-01-21 09:20
Category: iOS
Tags: iOS, util, base64
Slug: ios-utils-code-001


###常用代码

####Base64
```obj
NSString *decodeString = @"Raja";

---Encode String---

NSData *encodeData = [decodeString dataUsingEncoding:NSUTF8StringEncoding];
NSString *base64String = [encodeData base64EncodedStringWithOptions:0];
DLog(@"Encode String Value: %@", base64String);

---Decode String---

NSData *decodedData = [[NSData alloc] initWithBase64EncodedString:base64String options:0];
NSString *decodedString = [[NSString alloc] initWithData:decodedData encoding:NSUTF8StringEncoding];
DLog(@"Decode String Value: %@", decodedString);  
```