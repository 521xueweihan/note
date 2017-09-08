[toc]
12333
## 异常情况
异常响应内容如下。

### 1. 未登录
**status_code:** 401

```
response:
{
	"message": "需要登录"
}
```

### 2. 参数错误
**status_code:** 400

```
response:
{
	"message": "参数错误"
}
```

### 3. 已存在
**status_code:** 409

```
response:
{
	"message": "已存在"
}
```

## 1. 用户收藏功能
**该功能必须用户登录**

### 1.1 收藏夹
**功能描述：** 每个收藏的项目都所属于某个收藏夹。如用户没有收藏夹，会在触发“收藏”或访问”个人首页”的收藏夹页面时，自动创建一个“默认收藏夹”。

#### 1.1.1 获取用户所有的收藏夹
模板渲染，**api 接口查看 1.2.1**

#### 1.1.2 创建收藏夹
**url:** `/profile/collection/`

**method:** `POST`

**request args:**
- name: 收藏夹名称（require）

**successful response:**
```
{
	"message": "创建收藏夹 name 成功"
}
```

#### 1.1.3 更新收藏夹
**url:** `/profile/collection/`

**method:** `PUT`

**request args:**
- name: 收藏夹名称（require）

**successful response:**
```
{
	"message": "更新收藏夹 name 成功"
}
```

#### 1.1.3 删除收藏夹
**url:** `/profile/collection/`

**method:** `DELETE`

**request args:**
- collection_id: 收藏夹 id（require）

**successful response:**
```
{
	"message": "更新收藏夹成功"
}
```

### 1.2 收藏项目
**功能描述：** 把项目收藏到某一个收藏夹下，以供随时查看和使用

#### 1.2.1 获取用户所有的收藏夹
**url:** `/profile/collection/project/`

**method:** `GET`

**request args:**
- project_id: 已收藏的项目 id（require）

**successful response:**
```
{
  "payload": [
    {
      "create_time": "Tue, 08 Aug 2017 15:11:13 GMT",
      "id": 1,
      "name": "默认收藏夹",
      "status": 1,
      "update_time": "Tue, 08 Aug 2017 15:11:13 GMT",
      "uuid": 26452193
    }
  ]
}
```

#### 1.2.2 获取一个已收藏项目信息
**url:** `/profile/collection/project/`

**method:** `GET`

**request args:**
- project_id: 已收藏的项目 id（require）

**successful response:**
```
{
  "payload": {
    "collection": {
      "create_time": "Tue, 08 Aug 2017 15:11:13 GMT",
      "id": 1,
      "name": "默认收藏夹",
      "status": 1,
      "update_time": "Tue, 08 Aug 2017 15:11:13 GMT",
      "uuid": 26452193
    },
    "create_time": "Tue, 08 Aug 2017 15:11:14 GMT",
    "id": 1,
    "name": "VerificationCode",
    "project_url": "https://github.com/eatage/VerificationCode",
    "status": 1,
    "update_time": "Tue, 08 Aug 2017 15:11:14 GMT"
  }
}
```

#### 1.2.3 获取一个已收藏夹下所有项目信息
**url:** `/profile/collection/project/`

**method:** `GET`

**request args:**
- collection_id: 收藏夹 id（require）

**successful response:**
```
{
  "payload": [
    {
      "collection": {
        "create_time": "Tue, 08 Aug 2017 15:11:13 GMT",
        "id": 1,
        "name": "默认收藏夹",
        "status": 1,
        "update_time": "Tue, 08 Aug 2017 15:11:13 GMT",
        "uuid": 26452193
      },
      "create_time": "Tue, 08 Aug 2017 15:11:14 GMT",
      "id": 1,
      "name": "VerificationCode",
      "project_url": "https://github.com/eatage/VerificationCode",
      "status": 1,
      "update_time": "Tue, 08 Aug 2017 15:11:14 GMT"
    },
    {
      "collection": {
        "create_time": "Tue, 08 Aug 2017 15:11:13 GMT",
        "id": 1,
        "name": "默认收藏夹",
        "status": 1,
        "update_time": "Tue, 08 Aug 2017 15:11:13 GMT",
        "uuid": 26452193
      },
      "create_time": "Tue, 08 Aug 2017 15:19:16 GMT",
      "id": 2,
      "name": "Tinyhttpd",
      "project_url": "https://github.com/EZLippi/Tinyhttpd",
      "status": 1,
      "update_time": "Tue, 08 Aug 2017 15:19:16 GMT"
    }]
}
```

#### 1.2.4 收藏项目
**url:** `/profile/collection/project/`

**method:** `POST`

**request args:**
- collection_id: 收藏夹 id（require）
- project_name: 项目名称（require）
- project_url: 项目地址（require）

**successful response:**
```
{  
	"message": "收藏 useful-scripts 成功",
	"payload": {
		"collect_project_id": 24,
		"project_id": 301
	}
}
```

#### 1.2.5 更新收藏项目信息
**url:** `/profile/collection/project/`

**method:** `POST`

**request args:**
- collection_id: 收藏夹 id（require）
- project_id: 项目 id（require）
- project_name: 项目名称（require）

**successful response:**
```
{
	"message": "更新项目 project_name 成功",
}
```

#### 1.2.5 删除已收藏项目
**url:** `/profile/collection/project/`

**method:** `DELETE`

**request args:**
- project_id: 项目 id（require）

**successful response:**
```
{
	"message": "移除收藏项目成功",
}
```
