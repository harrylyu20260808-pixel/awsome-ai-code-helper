// 全局模板数据
const allTemplates = {
    functions: [
        {
            title: 'Sum Function / 求和函数',
            description: 'A function that accepts two parameters and returns their sum / 接受两个参数并返回它们的和',
            content: `You are a Python programming beginner. Please help me write a function that can:\n\n1. Accept two parameters (like a and b) / 1. 接受两个参数（比如a和b）\n2. Calculate the sum of these two parameters / 2. 计算这两个参数的和\n3. Return the calculation result / 3. 返回计算结果\n4. Code should be simple and easy to understand, add comments / 4. 代码要简单易懂，添加注释\n\nPlease return complete Python code with simple usage examples. / 请返回完整的Python代码，并附带简单的使用示例。`
        },
        {
            title: 'Age Judgment / 判断年龄',
            description: 'A function that determines if age is adult or minor / 判断年龄是成年人还是未成年人',
            content: `You are a Python programming beginner. Please help me write a function that can:\n\n1. Accept a person's age as a parameter / 1. 接收一个人的年龄作为参数\n2. Determine if the age is adult or minor / 2. 判断这个年龄是成年人还是未成年人\n   - 18 years or above is adult /   - 大于等于18岁是成年人\n   - Below 18 is minor /   - 小于18岁是未成年人\n3. Return "Adult" or "Minor" / 3. 返回"Adult"或"Minor"\n4. Add comments explaining each step / 4. 添加注释说明每一步\n\nPlease return complete Python code. / 请返回完整的Python代码。`
        },
        {
            title: 'String Length / 字符串长度',
            description: 'A function that calculates string length / 计算字符串的长度',
            content: `You are a Python programming beginner. Please help me write a function that can:\n\n1. Accept a string as a parameter / 1. 接收一个字符串作为参数\n2. Calculate the length of this string (how many characters) / 2. 计算这个字符串的长度（有多少个字符）\n3. Return the string length / 3. 返回字符串的长度\n4. Add comments explaining each step / 4. 添加注释说明每一步\n\nPlease return complete Python code with usage examples. / 请返回完整的Python代码和示例用法。`
        },
        {
            title: 'Maximum Value Function / 最大值函数',
            description: 'A function that finds the maximum of two numbers / 找出两个数字中的最大值',
            content: `You are a Python programming beginner. Please help me write a function that can:\n\n1. Accept two numbers as parameters / 1. 接收两个数字作为参数\n2. Compare these two numbers / 2. 比较这两个数字\n3. Return the larger number / 3. 返回较大的那个数字\n4. Add comments explaining each step / 4. 添加注释说明每一步\n\nPlease return complete Python code. / 请返回完整的Python代码。`
        },
        {
            title: 'Two Numbers Multiplication / 两个数相乘',
            description: 'A function that multiplies two numbers / 计算两个数字的乘积',
            content: `You are a Python programming beginner. Please help me write a function that can:\n\n1. Accept two numbers as parameters / 1. 接收两个数字作为参数\n2. Calculate the product of these two numbers / 2. 计算这两个数字的乘积\n3. Return the product result / 3. 返回乘积结果\n4. Add comments explaining each step / 4. 添加注释说明每一步\n\nPlease return complete Python code. / 请返回完整的Python代码。`
        }
    ],
    loop: [
        {
            title: 'Print 1 to 10 with for Loop / 使用for循环打印1到10',
            description: 'Use for loop to print numbers 1 to 10 / 使用for循环打印数字1到10',
            content: `You are a Python programming beginner. Please help me write a program that can:\n\n1. Use for loop / 1. 使用for循环\n2. Print numbers 1 to 10 / 2. 打印数字1到10\n3. Print one number per line / 3. 每行打印一个数字\n4. Add comments explaining each step / 4. 添加注释说明每一步\n\nPlease return complete Python code. / 请返回完整的Python代码。`
        },
        {
            title: 'Calculate 1 to 100 Sum / 计算1到100的和',
            description: 'Use for loop to calculate sum from 1 to 100 / 使用for循环计算1到100的总和',
            content: `You are a Python programming beginner. Please help me write a program that can:\n\n1. Use for loop / 1. 使用for循环\n2. Calculate the sum of all integers from 1 to 100 / 2. 计算1到100所有整数的和\n3. Output the calculation result / 3. 输出计算结果\n4. Add comments explaining each step / 4. 添加注释说明每一步\n\nPlease return complete Python code. / 请返回完整的Python代码。`
        },
        {
            title: 'Iterate Through List / 遍历列表',
            description: 'Use for loop to iterate through a list / 使用for循环遍历列表',
            content: `You are a Python programming beginner. Please help me write a program that can:\n\n1. Create a fruits list: ["apple", "banana", "orange", "grape"] / 1. 创建一个水果列表：["apple", "banana", "orange", "grape"]\n2. Use for loop to iterate through this list / 2. 使用for循环遍历这个列表\n3. Print the name of each fruit one by one / 3. 逐个打印每个水果的名称\n4. Add comments explaining each step / 4. 添加注释说明每一步\n\nPlease return complete Python code. / 请返回完整的Python代码。`
        },
        {
            title: 'Counting Days / 倒计时',
            description: 'Use while loop to count down from 10 to 1 / 使用while循环从10倒计时到1',
            content: `You are a Python programming beginner. Please help me write a program that can:\n\n1. Use while loop / 1. 使用while循环\n2. Count down from 10 to 1 / 2. 从10倒计时到1\n3. Display current number each time / 3. 每次显示当前数字\n4. Add comments explaining each step / 4. 添加注释说明每一步\n\nPlease return complete Python code. / 请返回完整的Python代码。`
        },
        {
            title: 'Fibonacci Sequence / 斐波那契数列',
            description: 'Return first n terms of Fibonacci sequence / 返回斐波那契数列的前n项',
            content: `You are a Python programming beginner. Please help me write a function that can:\n\n1. Accept a number n / 1. 接收一个数字n\n2. Return the first n terms of Fibonacci sequence / 2. 返回斐波那契数列的前n项\n3. Fibonacci sequence: 0, 1, 1, 2, 3, 5, 8, 13, ... / 3. 斐波那契数列：0, 1, 1, 2, 3, 5, 8, 13, ...\n4. Add comments explaining each step / 4. 添加注释说明每一步\n\nPlease return complete Python code. / 请返回完整的Python代码。`
        }
    ],
    'control-structure': [
        {
            title: 'Simple if Judgment / 简单的if判断',
            description: 'Determine if number is positive, negative, or zero / 判断数字是正数、负数还是0',
            content: `You are a Python programming beginner. Please help me write a program that can:\n\n1. Let user input a number / 1. 让用户输入一个数字\n2. Determine if this number is positive, negative, or zero / 2. 判断这个数字是正数、负数还是0\n3. Output corresponding message / 3. 输出相应的提示\n4. Add comments explaining each step / 4. 添加注释说明每一步\n\nPlease return complete Python code. / 请返回完整的Python代码。`
        },
        {
            title: 'if-elif-else Judgment / if-elif-else判断',
            description: 'Grade based on score (0-100) / 根据分数判断等级',
            content: `You are a Python programming beginner. Please help me write a program that can:\n\n1. Let user input a score (0-100) / 1. 让用户输入一个分数（0-100）\n2. Output grade based on score / 2. 根据分数输出等级\n   - Above 90: Excellent /   - 90分以上：优秀\n   - 80-89: Good /   - 80-89分：良好\n   - 70-79: Average /   - 70-79分：中等\n   - 60-69: Pass /   - 60-69分：及格\n   - Below 60: Fail /   - 60分以下：不及格\n3. Add comments explaining each step / 3. 添加注释说明每一步\n\nPlease return complete Python code. / 请返回完整的Python代码。`
        },
        {
            title: 'Guess Number Game / 猜数字游戏',
            description: 'Guess number between 1-100 with 5 attempts / 猜1-100之间的数字，最多5次机会',
            content: `You are a Python programming beginner. Please help me write a program that can:\n\n1. Computer randomly generates a number from 1 to 100 / 1. 电脑随机生成一个1到100的数字\n2. User inputs their guessed number / 2. 用户输入自己猜的数字\n3. If guess is correct, prompt "Congratulations!" / 3. 如果猜对了，提示"Congratulations!"\n4. If guess is wrong, prompt "Too high" or "Too low" / 4. 如果猜错了，提示"Too high"或"Too low"\n5. Maximum 5 attempts allowed / 5. 最多允许猜5次\n6. Add comments explaining each step / 6. 添加注释说明每一步\n\nPlease return complete Python code. / 请返回完整的Python代码。`
        },
        {
            title: 'for Loop with Range / for循环配合range',
            description: 'Print numbers 0 to 9 using for loop / 使用for循环打印0到9的数字',
            content: `You are a Python programming beginner. Please help me write a program that can:\n\n1. Use for loop with range() / 1. 使用for循环配合range()\n2. Print numbers 0 to 9 / 2. 打印0到9的数字\n3. Add comments explaining each step / 3. 添加注释说明每一步\n\nPlease return complete Python code. / 请返回完整的Python代码。`
        },
        {
            title: 'Nested Loops / 嵌套循环',
            description: 'Print multiplication table (9x9) / 打印九九乘法表',
            content: `You are a Python programming beginner. Please help me write a program that can:\n\n1. Use nested for loops / 1. 使用双重for循环\n2. Print a multiplication table (9x9) / 2. 打印九九乘法表\n3. Format nicely and align properly / 3. 格式美观，对齐整齐\n4. Add comments explaining each step / 4. 添加注释说明每一步\n\nPlease return complete Python code. / 请返回完整的Python代码。`
        }
    ],
    class: [
        {
            title: 'Student Class / 学生类',
            description: 'Define a Student class with attributes and method / 定义一个Student类，包含属性和方法',
            content: `You are a Python programming beginner. Please help me write a program that can:\n\n1. Define a "Student" class / 1. 定义一个"Student"类\n2. Include attributes: name, age, score / 2. 包含属性：name（姓名）、age（年龄）、score（分数）\n3. Include a method to print student information / 3. 包含一个打印学生信息的方法\n4. Create 2 student objects and print their info / 4. 创建2个学生对象并打印信息\n5. Add comments explaining each step / 5. 添加注释说明每一步\n\nPlease return complete Python code. / 请返回完整的Python代码。`
        },
        {
            title: 'Bank Account Class / 银行账户类',
            description: 'Create a BankAccount class with deposit/withdraw methods / 创建一个BankAccount类，包含存钱/取钱方法',
            content: `You are a Python programming beginner. Please help me write a program that can:\n\n1. Define a "BankAccount" class / 1. 定义一个"BankAccount"类\n2. Include attributes: account_number, account_name, balance / 2. 包含属性：account_number（账户号）、account_name（账户名）、balance（余额）\n3. Include methods: deposit, withdraw, check_balance / 3. 包含方法：deposit（存钱）、withdraw（取钱）、check_balance（查询余额）\n4. Create an account and test all methods / 4. 创建一个账户对象并测试所有方法\n5. Add comments explaining each step / 5. 添加注释说明每一步\n\nPlease return complete Python code. / 请返回完整的Python代码。`
        },
        {
            title: 'Circle Class / 圆形类',
            description: 'Create a Circle class with area and circumference methods / 创建一个Circle类，包含面积和周长方法',
            content: `You are a Python programming beginner. Please help me write a program that can:\n\n1. Define a "Circle" class / 1. 定义一个"Circle"类\n2. Include attribute: radius / 2. 包含属性：radius（半径）\n3. Include methods: calculate_area, calculate_circumference / 3. 包含方法：calculate_area（计算面积）、calculate_circumference（计算周长）\n4. Create a circle object and test methods / 4. 创建一个圆形对象并测试方法\n5. Add comments explaining each step / 5. 添加注释说明每一步\n\nPlease return complete Python code. / 请返回完整的Python代码。`
        },
        {
            title: 'Book Class / 书籍类',
            description: 'Create a Book class with title, author, price, pages / 创建一个Book类，包含书名、作者、价格、页数',
            content: `You are a Python programming beginner. Please help me write a program that can:\n\n1. Define a "Book" class / 1. 定义一个"Book"类\n2. Include attributes: title, author, price, pages / 2. 包含属性：title（书名）、author（作者）、price（价格）、pages（页数）\n3. Include a method to display book info / 3. 包含一个显示书籍信息的方法\n4. Create 3 book objects and display their info / 4. 创建3本书的对象并显示信息\n5. Add comments explaining each step / 5. 添加注释说明每一步\n\nPlease return complete Python code. / 请返回完整的Python代码。`
        },
        {
            title: 'Rectangle Class / 矩形类',
            description: 'Create a Rectangle class with area and perimeter methods / 创建一个Rectangle类，包含面积和周长方法',
            content: `You are a Python programming beginner. Please help me write a program that can:\n\n1. Define a "Rectangle" class / 1. 定义一个"Rectangle"类\n2. Include attributes: width, height / 2. 包含属性：width（宽）、height（高）\n3. Include methods: calculate_area, calculate_perimeter / 3. 包含方法：calculate_area（计算面积）、calculate_perimeter（计算周长）\n4. Create 2 rectangle objects and calculate area and perimeter / 4. 创建2个矩形对象并计算面积和周长\n5. Add comments explaining each step / 5. 添加注释说明每一步\n\nPlease return complete Python code. / 请返回完整的Python代码。`
        }
    ],
    'file-operation': [
        {
            title: 'Write to File / 写入文件',
            description: 'Create a file and write content to it / 创建文件并写入内容',
            content: `You are a Python programming beginner. Please help me write a program that can:\n\n1. Create a text file (like: todo.txt) / 1. 创建一个文本文件（比如：todo.txt）\n2. Write the following content: / 2. 写入以下内容：\n   - Line 1: Task 1 /   - 第1行：任务1\n   - Line 2: Task 2 /   - 第2行：任务2\n   - Line 3: Task 3 /   - 第3行：任务3\n3. Close the file / 3. 关闭文件\n4. Add comments explaining each step / 4. 添加注释说明每一步\n\nPlease return complete Python code. / 请返回完整的Python代码。`
        },
        {
            title: 'Read from File / 读取文件',
            description: 'Open a file and read its content / 打开文件并读取内容',
            content: `You are a Python programming beginner. Please help me write a program that can:\n\n1. Open a text file (write some content first) / 1. 打开一个文本文件（先写入一些内容）\n2. Read all content of the file / 2. 读取文件的所有内容\n3. Print the read content / 3. 打印读取到的内容\n4. Add comments explaining each step / 4. 添加注释说明每一步\n\nPlease return complete Python code. / 请返回完整的Python代码。`
        },
        {
            title: 'Read File Line by Line / 逐行读取文件',
            description: 'Read file content line by line / 使用for循环逐行读取文件',
            content: `You are a Python programming beginner. Please help me write a program that can:\n\n1. Create a file with multiple lines of text / 1. 创建一个包含多行文字的文件\n2. Use for loop to read the file line by line / 2. 使用for循环逐行读取文件\n3. Print each line's content / 3. 打印每一行的内容\n4. Add comments explaining each step / 4. 添加注释说明每一步\n\nPlease return complete Python code. / 请返回完整的Python代码。`
        },
        {
            title: 'Students in File / 文件中的学生信息',
            description: 'Read student info from a file / 从文件读取学生信息',
            content: `You are a Python programming beginner. Please help me write a program that can:\n\n1. Create a student info file (students.txt), each line contains: / 1. 创建一个学生信息文件（students.txt），每行包含：\n   - name and age (comma separated) /   - 姓名和年龄（用逗号分隔）\n   - Example: Zhang San,18 /   - 例如：Zhang San,18\n2. Read the file and display all student info / 2. 读取文件并显示所有学生信息\n3. Add comments explaining each step / 3. 添加注释说明每一步\n\nPlease return complete Python code. / 请返回完整的Python代码。`
        },
        {
            title: 'Count Words in File / 统计文件中的单词数',
            description: 'Count word frequency in a file / 统计文件中单词的出现次数',
            content: `You are a Python programming beginner. Please help me write a program that can:\n\n1. Create a text file with some English sentences / 1. 创建一个包含一些英文句子的文件\n2. Read file content / 2. 读取文件内容\n3. Count how many times each word appears (separated by spaces) / 3. 统计每个单词出现了多少次（用空格分隔）\n4. Output total word count / 4. 输出单词总数\n5. Add comments explaining each step / 5. 添加注释说明每一步\n\nPlease return complete Python code. / 请返回完整的Python代码。`
        },
        {
            title: 'Append to File / 追加内容到文件',
            description: 'Append content to an existing file / 向现有文件追加内容',
            content: `You are a Python programming beginner. Please help me write a program that can:\n\n1. Append a new task to existing todo.txt file / 1. 在已有的todo.txt文件中追加一条新任务\n2. Display all current content of the file / 2. 显示文件现在的所有内容\n3. Add comments explaining each step / 3. 添加注释说明每一步\n\nPlease return complete Python code. / 请返回完整的Python代码。`
        }
    ],
    'data-processing': [
        {
            title: 'Count Word Occurrences / 统计单词出现次数',
            description: 'Count how many times each word appears in a list / 统计列表中每个单词出现的次数',
            content: `You are a Python programming beginner. Please help me write a program that can:\n\n1. Create a list containing multiple words / 1. 创建一个包含多个单词的列表\n2. Count how many times each word appears / 2. 统计每个单词出现的次数\n3. Output the count results / 3. 输出统计结果\n4. Add comments explaining each step / 4. 添加注释说明每一步\n\nPlease return complete Python code. / 请返回完整的Python代码。`
        },
        {
            title: 'Filter Even Numbers / 筛选偶数',
            description: 'Filter even numbers from a list / 从列表筛选出所有的偶数',
            content: `You are a Python programming beginner. Please help me write a program that can:\n\n1. Create a list with 10 numbers / 1. 创建一个包含10个数字的列表\n2. Use list comprehension to filter all even numbers / 2. 使用列表推导式筛选出所有的偶数\n3. Output the filtered results / 3. 输出筛选结果\n4. Add comments explaining each step / 4. 添加注释说明每一步\n\nPlease return complete Python code. / 请返回完整的Python代码。`
        },
        {
            title: 'Dictionary Basics / 字典基础',
            description: 'Create and use a dictionary / 创建并使用字典',
            content: `You are a Python programming beginner. Please help me write a program that can:\n\n1. Create a simple dictionary: / 1. 创建一个简单字典：\n   - key: fruit name /   - 键：水果名\n   - value: price /   - 值：价格\n   - Example: {"apple":5, "banana":3, "orange":4} /   - 例如：{"apple":5, "banana":3, "orange":4}\n2. Iterate through dictionary, print all fruits and their prices / 2. 遍历字典，打印所有水果及其价格\n3. Add comments explaining each step / 3. 添加注释说明每一步\n\nPlease return complete Python code. / 请返回完整的Python代码。`
        },
        {
            title: 'Sort Dictionary by Value / 按值排序字典',
            description: 'Sort dictionary by value from low to high / 按价格从低到高排序字典',
            content: `You are a Python programming beginner. Please help me write a program that can:\n\n1. Create a dictionary with some fruit prices / 1. 创建一个包含几个水果价格的字典\n2. Sort by price from low to high / 2. 按价格从低到高排序\n3. Output sorted results / 3. 输出排序后的结果\n4. Add comments explaining each step / 4. 添加注释说明每一步\n\nPlease return complete Python code. / 请返回完整的Python代码。`
        },
        {
            title: 'Sort List / 列表排序',
            description: 'Sort a list of numbers / 将列表按从小到大的顺序排序',
            content: `You are a Python programming beginner. Please help me write a program that can:\n\n1. Create a list with multiple numbers / 1. 创建一个包含多个数字的列表\n2. Sort the list from small to large / 2. 将列表按从小到大的顺序排序\n3. Output sorted list / 3. 输出排序后的列表\n4. Add comments explaining each step / 4. 添加注释说明每一步\n\nPlease return complete Python code. / 请返回完整的Python代码。`
        },
        {
            title: 'Find Min and Max in List / 找出最小值和最大值',
            description: 'Find the minimum and maximum values in a list / 找出列表中的最小值和最大值',
            content: `You are a Python programming beginner. Please help me write a program that can:\n\n1. Create a list with 10 numbers / 1. 创建一个包含10个数字的列表\n2. Find the minimum and maximum values in the list / 2. 找出列表中的最小值和最大值\n3. Output min and max values / 3. 输出最小值和最大值\n4. Add comments explaining each step / 4. 添加注释说明每一步\n\nPlease return complete Python code. / 请返回完整的Python代码。`
        }
    ],
    database: [
        {
            title: 'Create Table / 创建表',
            description: 'Create a student table with SQLite / 使用SQLite创建学生表',
            content: `You are a Python programming beginner. Please help me write a program that can:\n\n1. Use SQLite database / 1. 使用SQLite数据库\n2. Create a "student" table with fields: id, name, age, score / 2. 创建一个"student"表，包含字段：id（主键）、name（姓名）、age（年龄）、score（分数）\n3. Add comments explaining each step / 3. 添加注释说明每一步\n\nPlease return complete Python code. / 请返回完整的Python代码。`
        },
        {
            title: 'Insert Data / 插入数据',
            description: 'Insert data into student table / 向学生表插入数据',
            content: `You are a Python programming beginner. Please help me write a program that can:\n\n1. Use the created student table / 1. 使用已创建的学生表\n2. Insert 3 student records / 2. 插入3条学生数据\n3. Commit transaction / 3. 提交事务\n4. Add comments explaining each step / 4. 添加注释说明每一步\n\nPlease return complete Python code. / 请返回完整的Python代码。`
        },
        {
            title: 'Query All Data / 查询所有数据',
            description: 'Query all data from student table / 查询学生表中的所有数据',
            content: `You are a Python programming beginner. Please help me write a program that can:\n\n1. Query all data from student table / 1. 查询学生表中的所有数据\n2. Print query results / 2. 打印查询结果\n3. Add comments explaining each step / 3. 添加注释说明每一步\n\nPlease return complete Python code. / 请返回完整的Python代码。`
        },
        {
            title: 'Query Specific Data / 查询特定数据',
            description: 'Query students with score > 80 / 查询分数大于80的学生信息',
            content: `You are a Python programming beginner. Please help me write a program that can:\n\n1. Query students with score greater than 80 / 1. 查询分数大于80的学生信息\n2. Print query results / 2. 打印查询结果\n3. Add comments explaining each step / 3. 添加注释说明每一步\n\nPlease return complete Python code. / 请返回完整的Python代码。`
        },
        {
            title: 'Update Data / 更新数据',
            description: 'Update student score / 更新学生分数',
            content: `You are a Python programming beginner. Please help me write a program that can:\n\n1. Increase a student's score by 10 points / 1. 将某个学生的分数提高10分\n2. Commit transaction / 2. 提交事务\n3. Query and print updated data / 3. 查询并打印更新后的数据\n4. Add comments explaining each step / 4. 添加注释说明每一步\n\nPlease return complete Python code. / 请返回完整的Python代码。`
        },
        {
            title: 'Delete Data / 删除数据',
            description: 'Delete a student record / 删除某个学生记录',
            content: `You are a Python programming beginner. Please help me write a program that can:\n\n1. Delete a student (by id) / 1. 删除某个学生（根据id）\n2. Commit transaction / 2. 提交事务\n3. Query and print all data after deletion / 3. 查询并打印删除后的所有数据\n4. Add comments explaining each step / 4. 添加注释说明每一步\n\nPlease return complete Python code. / 请返回完整的Python代码。`
        }
    ],
    'web-development': [
        {
            title: 'Simple Web Interface / 简单Web界面',
            description: 'Create a web interface with input and button / 创建包含输入框和按钮的Web界面',
            content: `You are a Python programming beginner. Please help me write a program that can:\n\n1. Create a simple web interface / 1. 创建一个简单的Web界面\n2. Display title: "My First Web Program" / 2. 显示标题："My First Web Program"\n3. Display an input box / 3. 显示一个输入框\n4. Display a button / 4. 显示一个按钮\n5. When button is clicked, display input content / 5. 点击按钮后显示输入的内容\n6. Use FastAPI framework / 6. 使用FastAPI框架\n7. Add comments explaining each step / 7. 添加注释说明每一步\n\nPlease return complete Python code. / 请返回完整的Python代码。`
        },
        {
            title: 'Calculator Web App / 计算器Web应用',
            description: 'Create a calculator web application / 创建一个计算器Web应用',
            content: `You are a Python programming beginner. Please help me write a program that can:\n\n1. Create a simple web application / 1. 创建一个简单的Web应用\n2. Include two number input boxes and an operator selector (+, -, *, /) / 2. 包含两个数字输入框和一个运算符选择（+、-、*、/）\n3. When button is clicked, calculate result and display / 3. 点击按钮后计算结果并显示\n4. Use FastAPI framework / 4. 使用FastAPI框架\n5. Add comments explaining each step / 5. 添加注释说明每一步\n\nPlease return complete Python code. / 请返回完整的Python代码。`
        },
        {
            title: 'Student Management Web / 学生管理Web界面',
            description: 'Create student management web interface / 创建学生管理Web界面',
            content: `You are a Python programming beginner. Please help me write a program that can:\n\n1. Create a web interface / 1. 创建一个Web界面\n2. Display student list / 2. 显示学生列表\n3. Allow adding new students / 3. 允许添加新学生\n4. Allow deleting students / 4. 允许删除学生\n5. Use FastAPI framework / 5. 使用FastAPI框架\n6. Add comments explaining each step / 6. 添加注释说明每一步\n\nPlease return complete Python code. / 请返回完整的Python代码。`
        }
    ],
    algorithms: [
        {
            title: 'Two Sum / 两数之和',
            description: 'Find two numbers that sum to target / 找到两个数使它们等于目标值',
            content: `You are a Python programming beginner. Please help me write a function that can:\n\n1. Accept a list of integers and a target value / 1. 接收一个整数列表和一个目标值\n2. Find two numbers in the list that sum to the target value / 2. 找到列表中两个数相加等于目标值的两个数字\n3. Return the indices of these two numbers / 3. 返回这两个数字的索引\n4. Each number can only be used once / 4. 每个数字只能使用一次\n5. Add comments explaining each step / 5. 添加注释说明每一步\n\nPlease return complete Python code. / 请返回完整的Python代码。`
        },
        {
            title: 'Fibonacci Sequence / 斐波那契数列',
            description: 'Return first n terms of Fibonacci sequence / 返回斐波那契数列的前n项',
            content: `You are a Python programming beginner. Please help me write a function that can:\n\n1. Accept a number n / 1. 接收一个数字n\n2. Return the first n terms of Fibonacci sequence / 2. 返回斐波那契数列的前n项\n3. Fibonacci sequence: 0, 1, 1, 2, 3, 5, 8, 13, ... / 3. 斐波那契数列：0, 1, 1, 2, 3, 5, 8, 13, ...\n4. Add comments explaining each step / 4. 添加注释说明每一步\n\nPlease return complete Python code. / 请返回完整的Python代码。`
        },
        {
            title: 'Reverse Array / 反转数组',
            description: 'Reverse a list from right to left / 将列表从右到左反转',
            content: `You are a Python programming beginner. Please help me write a function that can:\n\n1. Accept a list of integers / 1. 接收一个整数列表\n2. Reverse the list (from right to left) / 2. 将列表反转（从右到左）\n3. Return the reversed list / 3. 返回反转后的列表\n4. Add comments explaining each step / 4. 添加注释说明每一步\n\nPlease return complete Python code. / 请返回完整的Python代码。`
        },
        {
            title: 'Palindrome Check / 回文检查',
            description: 'Check if string is palindrome / 检查字符串是否是回文',
            content: `You are a Python programming beginner. Please help me write a function that can:\n\n1. Accept a string / 1. 接收一个字符串\n2. Determine if this string is a palindrome (reads the same forwards and backwards) / 2. 判断这个字符串是否是回文（正读和反读一样）\n3. Return True or False / 3. 返回True或False\n4. Add comments explaining each step / 4. 添加注释说明每一步\n\nPlease return complete Python code. / 请返回完整的Python代码。`
        }
    ],
    openclaw: [
        {
            title: 'OpenCLAW Beginner / OpenCLAW初学者',
            description: 'Create a simple greeting function with OpenCLAW / 创建一个简单的问候函数',
            content: `I am a Python programming beginner. Please help me use OpenCLAW to write a program that can:\n\n1. Accept a user's name as input / 1. 接受用户名字作为输入\n2. Greet the user with a friendly message / 2. 用友好的消息问候用户\n3. Include comments explaining the OpenCLAW concepts / 3. 包含注释说明OpenCLAW的概念\n4. Code should be simple and easy to understand / 4. 代码要简单易懂\n\nPlease return complete Python code with OpenCLAW implementation. / 请返回完整的Python代码和OpenCLAW实现。`
        },
        {
            title: 'OpenCLAW Data Processing / OpenCLAW数据处理',
            description: 'Process a list of numbers with OpenCLAW / 使用OpenCLAW处理数字列表',
            content: `I am a Python programming beginner. Please help me use OpenCLAW to write a program that can:\n\n1. Create a list of 10 random numbers / 1. 创建一个包含10个随机数字的列表\n2. Use OpenCLAW to process and transform the data / 2. 使用OpenCLAW处理和转换数据\n3. Calculate the sum and average of the numbers / 3. 计算数字的总和和平均值\n4. Display the results clearly / 4. 清晰地显示结果\n5. Add comments explaining OpenCLAW concepts / 5. 添加注释说明OpenCLAW概念\n\nPlease return complete Python code. / 请返回完整的Python代码。`
        },
        {
            title: 'OpenCLAW File I/O / OpenCLAW文件操作',
            description: 'Read and write files using OpenCLAW / 使用OpenCLAW读写文件',
            content: `I am a Python programming beginner. Please help me use OpenCLAW to write a program that can:\n\n1. Read a text file containing student scores / 1. 读取一个包含学生分数的文本文件\n2. Use OpenCLAW to process the data / 2. 使用OpenCLAW处理数据\n3. Calculate the average score / 3. 计算平均分数\n4. Write the results to a new file / 4. 将结果写入新文件\n5. Add comments explaining the process / 5. 添加注释说明过程\n\nPlease return complete Python code. / 请返回完整的Python代码。`
        },
        {
            title: 'OpenCLAW Error Handling / OpenCLAW错误处理',
            description: 'Handle errors gracefully with OpenCLAW / 使用OpenCLAW优雅地处理错误',
            content: `I am a Python programming beginner. Please help me use OpenCLAW to write a program that can:\n\n1. Try to read a file that might not exist / 1. 尝试读取可能不存在的文件\n2. Handle different types of errors (FileNotFound, etc.) / 2. 处理不同类型的错误（FileNotFound等）\n3. Display user-friendly error messages / 3. 显示用户友好的错误消息\n4. Use OpenCLAW error handling patterns / 4. 使用OpenCLAW错误处理模式\n5. Add comments explaining error handling concepts / 5. 添加注释说明错误处理概念\n\nPlease return complete Python code. / 请返回完整的Python代码。`
        },
        {
            title: 'OpenCLAW Modular Code / OpenCLAW模块化代码',
            description: 'Write modular code with functions and classes using OpenCLAW / 使用OpenCLAW编写包含函数和类的模块化代码',
            content: `I am a Python programming beginner. Please help me use OpenCLAW to write a program that can:\n\n1. Define a Calculator class with methods (add, subtract, multiply, divide) / 1. 定义一个Calculator类，包含方法（add, subtract, multiply, divide）\n2. Use OpenCLAW to implement these methods / 2. 使用OpenCLAW实现这些方法\n3. Create a simple interface to use the calculator / 3. 创建一个简单的界面来使用计算器\n4. Add comprehensive comments / 4. 添加详细的注释\n5. Include example usage / 5. 包含使用示例\n\nPlease return complete Python code with OpenCLAW implementation. / 请返回包含OpenCLAW实现的完整Python代码。`
        }
    ],
    claude: [
        {
            title: 'Claude Beginner Guide / Claude新手指南',
            description: 'Get started with Claude AI assistant / 开始使用Claude AI助手',
            content: `I am a Python programming beginner. I want to learn how to use Claude AI assistant effectively. Please help me:\n\n1. Understand what Claude can do for coding tasks / 1. 理解Claude可以为编码任务做什么\n2. Learn basic prompts I can use / 2. 学习我可以使用的基本prompt\n3. Get examples of helpful coding prompts / 3. 获取有用的编码prompt示例\n4. Understand best practices for using Claude / 4. 理解使用Claude的最佳实践\n5. Get started with my first coding task / 5. 开始我的第一个编码任务\n\nPlease provide a beginner-friendly guide to using Claude. / 请提供一个适合初学者的Claude使用指南。`
        },
        {
            title: 'Claude Code Explanation / Claude代码解释',
            description: 'Get detailed explanation of code using Claude / 使用Claude获取详细的代码解释',
            content: `I am a Python programming beginner. I need help understanding a piece of code:\n\n[code here] / 要理解的代码：\n[code here]\n\nPlease use Claude to help me:\n1. Explain the code's purpose in simple terms / 1. 用简单的术语解释代码的目的\n2. Break down the code line by line with explanations / 2. 逐行分解代码并解释\n3. Explain the key concepts and programming patterns used / 3. 解释使用的关键概念和编程模式\n4. Provide real-world analogies to help understanding / 4. 提供现实世界的类比来帮助理解\n5. Suggest what I should learn next / 5. 建议我应该学习什么\n\nPlease provide a comprehensive but beginner-friendly explanation. / 请提供一个全面但适合初学者的解释。`
        },
        {
            title: 'Claude Debugging Help / Claude调试帮助',
            description: 'Get debugging assistance from Claude / 从Claude获得调试帮助',
            content: `I am a Python programming beginner. I have a problem with my code:\n\nCurrent code:\n[code here] / 当前代码：\n[code here]\n\nError message:\n[insert error message here] / 错误消息：\n[在此处插入错误消息]\n\nPlease help me use Claude to:\n1. Identify the root cause of the problem / 1. 识别问题的根本原因\n2. Explain what went wrong in simple terms / 2. 用简单的术语解释哪里出了问题\n3. Generate corrected code / 3. 生成修正后的代码\n4. Suggest what I should learn to avoid this error / 4. 建议我应该学习什么以避免这个错误\n5. Provide similar examples for practice / 5. 提供类似的示例供练习\n\nPlease return a complete debugging solution. / 请返回完整的调试解决方案。`
        },
        {
            title: 'Claude Code Review / Claude代码审查',
            description: 'Get code review from Claude AI / 从Claude AI获得代码审查',
            content: `I am a Python programming beginner. Please help me improve my code using Claude:\n\n[code here] / 我的代码：\n[code here]\n\nPlease use Claude to review my code and:\n1. Point out any bugs or errors / 1. 指出任何错误或bug\n2. Suggest improvements for better performance / 2. 建议改进以提高性能\n3. Recommend cleaner, more Pythonic ways to write the code / 3. 推荐更清晰、更Pythonic的代码写法\n4. Explain best practices I'm not following / 4. 解释我不遵循的最佳实践\n5. Provide rewritten code with explanations / 5. 提供重写后的代码和解释\n\nPlease provide constructive feedback and a rewritten version of my code. / 请提供建设性的反馈和我代码的重写版本。`
        },
        {
            title: 'Claude Learning Path / Claude学习路径',
            description: 'Get personalized learning recommendations from Claude / 从Claude获得个性化的学习建议',
            content: `I am a Python programming beginner with [X years] of coding experience / 我是一个有[X年]编程经验的Python初学者\n\nMy current skills: / 我当前的技能：\n[list what you can do] / [列出你能做的]\n\nMy learning goals: / 我的学习目标：\n[list your goals] / [列出你的目标]\n\nPlease help me create a learning path using Claude:\n1. Suggest which topics I should learn first / 1. 建议我应该先学习哪些主题\n2. Recommend specific resources and examples / 2. 推荐具体的资源和示例\n3. Create a step-by-step learning plan / 3. 创建分步学习计划\n4. Suggest practice projects I can work on / 4. 建议我可以做的练习项目\n5. Explain how Claude can help at each stage / 5. 解释Claude如何在每个阶段提供帮助\n\nPlease provide a practical and achievable learning plan. / 请提供一个实用且可实现的学习计划。`
        }
    ],
    codex: [
        {
            title: 'Codex Code Generation / Codex代码生成',
            description: 'Generate complete code solution using Codex / 使用Codex生成完整的代码解决方案',
            content: `I am a Python programming beginner. Please help me use Codex to:\n\n1. Analyze my requirements and generate complete code / 1. 分析我的需求并生成完整的代码\n2. Include all necessary imports and libraries / 2. 包含所有必要的导入和库\n3. Add detailed comments explaining each part / 3. 添加详细的注释说明每个部分\n4. Provide example usage demonstrating the code functionality / 4. 提供使用示例来展示代码功能\n5. Explain how the code works in simple terms / 5. 用简单的术语解释代码如何工作\n\nMy requirement is: [insert your requirement here] / 我的需求是：[在此处插入你的需求]\n\nPlease return complete Python code ready to run. / 请返回可以直接运行的完整Python代码。`
        },
        {
            title: 'Codex Debugging / Codex调试',
            description: 'Fix my code issues using Codex debugging tools / 使用Codex调试工具修复代码问题',
            content: `I am a Python programming beginner. I have a code problem:\n\nCurrent code:\n[code here] / 当前代码：\n[code here]\n\nError message:\n[insert error message here] / 错误消息：\n[在此处插入错误消息]\n\nPlease help me use Codex to:\n1. Identify the root cause of the error / 1. 识别错误的根本原因\n2. Generate corrected code / 2. 生成修正后的代码\n3. Explain what was wrong and how I fixed it / 3. 解释哪里出了问题以及如何修复\n4. Provide best practice suggestions / 4. 提供最佳实践建议\n5. Add comments explaining the fixes / 5. 添加注释说明修复内容\n\nPlease return the complete fixed code. / 请返回完整的修复后的代码。`
        },
        {
            title: 'Codex Code Explanation / Codex代码解释',
            description: 'Understand complex code using Codex explanation tools / 使用Codex解释工具理解复杂代码',
            content: `I am a Python programming beginner. I need help understanding this code:\n\nCode to understand:\n[code here] / 要理解的代码：\n[code here]\n\nPlease use Codex to help me:\n1. Explain what the code does in simple terms / 1. 用简单的术语解释代码的功能\n2. Break down the code line by line / 2. 逐行分解代码\n3. Explain key concepts and techniques used / 3. 解释使用的关键概念和技术\n4. Provide real-world analogies where helpful / 4. 在适当的地方提供现实世界的类比\n5. Suggest how I can learn and improve similar code / 5. 建议我如何学习和改进类似的代码\n\nPlease provide a clear, beginner-friendly explanation. / 请提供清晰、适合初学者的解释。`
        },
        {
            title: 'Codex Code Optimization / Codex代码优化',
            description: 'Optimize and improve code performance with Codex / 使用Codex优化和提升代码性能',
            content: `I am a Python programming beginner. Here is my current code:\n\n[code here] / 这是我的当前代码：\n[code here]\n\nPlease use Codex to help me:\n1. Analyze the current performance and efficiency / 1. 分析当前性能和效率\n2. Suggest optimizations (e.g., better algorithms, data structures) / 2. 建议优化（如更好的算法、数据结构）\n3. Provide optimized code with comments / 3. 提供优化后的代码和注释\n4. Explain the improvements and why they matter / 4. 解释改进内容以及为什么重要\n5. Show performance comparison if possible / 5. 如果可能，显示性能对比\n\nMy goal is: [insert optimization goal here] / 我的目标是：[在此处插入优化目标]\n\nPlease return the optimized code. / 请返回优化后的代码。`
        },
        {
            title: 'Codex Best Practices / Codex最佳实践',
            description: 'Learn Python best practices using Codex guidance / 使用Codex指导学习Python最佳实践',
            content: `I am a Python programming beginner. Please help me improve my code practices using Codex:\n\nCurrent code:\n[code here] / 当前代码：\n[code here]\n\nPlease guide me to:\n1. Refactor the code to follow Python best practices / 1. 重构代码以遵循Python最佳实践\n2. Improve code readability and organization / 2. 改善代码可读性和组织性\n3. Add proper docstrings and comments / 3. 添加适当的docstring和注释\n4. Suggest improvements for naming, structure, and style / 4. 建议改进命名、结构和风格\n5. Explain the best practices being applied / 5. 解释应用的最佳实践\n\nPlease return the refactored code with explanations. / 请返回重构后的代码和解释。`
        }
    ]
};

// 获取特定分类的模板
function getTemplatesForSection(sectionId) {
    let templates = [];

    if (allTemplates[sectionId]) {
        templates = [...allTemplates[sectionId]];
    }

    const customTemplates = JSON.parse(localStorage.getItem('customTemplates')) || [];
    templates = [...templates, ...customTemplates];

    return templates;
}

// 创建模板卡片
function createTemplateCard(template) {
    const card = document.createElement('div');
    card.className = 'template-card';

    const codeContent = template.content.trim();

    card.innerHTML = `
        <h3>${template.title}</h3>
        <p class="description">${template.description || 'Copy this prompt and send it to AI coding assistant to get code.'}</p>
        <pre class="code-preview">${escapeHtml(codeContent.substring(0, 200))}${codeContent.length > 200 ? '...' : ''}</pre>
        <button class="copy-btn" onclick="copyPrompt(this, \`${escapeJs(codeContent)}\`)">
            📋 Copy Prompt
        </button>
    `;

    // 添加编辑和删除按钮（仅对自定义模板）
    if (template.id) {
        card.innerHTML += `
            <button class="edit-btn" onclick="showCustomTemplateModal('${template.id}')" title="Edit template">✏️</button>
            <button class="delete-btn" onclick="deleteTemplate('${template.id}')" title="Delete template">🗑️</button>
        `;
    }

    return card;
}

// 复制Prompt
function copyPrompt(button, promptText) {
    navigator.clipboard.writeText(promptText).then(() => {
        button.innerHTML = '✅ Copied';
        button.classList.add('copied');

        setTimeout(() => {
            button.innerHTML = '📋 Copy Prompt';
            button.classList.remove('copied');
        }, 2000);
    }).catch(err => {
        alert('Failed to copy: ' + err);
    });
}

// 设置导航
function setupNavigation() {
    const navItems = document.querySelectorAll('.nav-item');

    navItems.forEach(item => {
        item.addEventListener('click', function() {
            const sectionId = this.getAttribute('data-section');
            showSection(sectionId);
        });
    });
}

// 显示指定section
function showSection(sectionId) {
    const navItems = document.querySelectorAll('.nav-item');
    navItems.forEach(n => n.classList.remove('active'));

    const sections = document.querySelectorAll('.section');
    sections.forEach(s => s.classList.remove('active'));

    const navItem = document.querySelector(`.nav-item[data-section="${sectionId}"]`);
    if (navItem) {
        navItem.classList.add('active');
    }

    const section = document.getElementById(sectionId);
    if (section) {
        section.classList.add('active');
    }

    window.scrollTo({ top: 0, behavior: 'smooth' });

    if (sectionId === 'custom') {
        const container = document.getElementById('customTemplateList');
        if (container) {
            container.innerHTML = '';
            loadTemplatesForSection('custom', container);
        }
    }
}

// 设置模态框事件监听器
function setupModalEvents() {
    document.querySelectorAll('.modal').forEach(modal => {
        modal.addEventListener('click', function(e) {
            if (e.target === this) {
                this.classList.add('hidden');
            }
        });
    });

    document.addEventListener('keydown', function(e) {
        if (e.key === 'Escape') {
            document.querySelectorAll('.modal:not(.hidden)').forEach(modal => {
                modal.classList.add('hidden');
            });
        }
    });
}

// HTML转义
function escapeHtml(text) {
    const div = document.createElement('div');
    div.textContent = text;
    return div.innerHTML;
}

// JavaScript字符串转义
function escapeJs(text) {
    return text.replace(/`/g, '\\`')
               .replace(/\$/g, '\\$')
               .replace(/\n/g, '\\n')
               .replace(/"/g, '\\"');
}

// 加载模板
function loadTemplates() {
    const sections = [
        { id: 'functions', title: 'Function Development Templates' },
        { id: 'loop', title: 'Loop Control Templates' },
        { id: 'control-structure', title: 'Control Structure Templates' },
        { id: 'class', title: 'Object-Oriented Templates' },
        { id: 'file-operation', title: 'File Operation Templates' },
        { id: 'data-processing', title: 'Data Processing Templates' },
        { id: 'database', title: 'Database Templates' },
        { id: 'web-development', title: 'Web Development Templates' },
        { id: 'algorithms', title: 'Algorithm Practice Templates' },
        { id: 'openclaw', title: 'OpenCLAW Templates' },
        { id: 'claude', title: 'Claude Code Templates' },
        { id: 'codex', title: 'Codex Templates' },
        { id: 'custom', title: 'Custom Templates' }
    ];

    sections.forEach(section => {
        const container = document.querySelector(`#${section.id} .template-list`);
        if (container) {
            loadTemplatesForSection(section.id, container);
        }
    });

    updateCustomCount();
}

// 加载特定分类的模板
function loadTemplatesForSection(sectionId, container) {
    const templates = getTemplatesForSection(sectionId);

    templates.forEach(template => {
        const card = createTemplateCard(template);
        container.appendChild(card);
    });
}

// 更新自定义模板计数
function updateCustomCount() {
    const customTemplates = JSON.parse(localStorage.getItem('customTemplates')) || [];
    const countEl = document.getElementById('customCount');
    if (countEl) {
        countEl.textContent = customTemplates.length;
    }
    updateCustomEmptyState();
}

// 更新空状态显示
function updateCustomEmptyState() {
    const customTemplates = JSON.parse(localStorage.getItem('customTemplates')) || [];
    const emptyState = document.getElementById('customEmptyState');

    if (emptyState) {
        if (customTemplates.length === 0) {
            emptyState.style.display = 'block';
        } else {
            emptyState.style.display = 'none';
        }
    }
}

// 初始化时隐藏空状态
function hideCustomEmptyState() {
    const emptyState = document.getElementById('customEmptyState');
    if (emptyState) {
        emptyState.style.display = 'none';
    }
}

// 保存模板到localStorage
function saveTemplateToStorage(template) {
    const customTemplates = JSON.parse(localStorage.getItem('customTemplates')) || [];

    if (template.id) {
        const index = customTemplates.findIndex(t => t.id === template.id);
        if (index !== -1) {
            customTemplates[index] = template;
        }
    } else {
        template.id = Date.now().toString();
        customTemplates.push(template);
    }

    try {
        localStorage.setItem('customTemplates', JSON.stringify(customTemplates));
        updateCustomEmptyState();
        return true;
    } catch (e) {
        console.error('Failed to save template:', e);
        alert('Failed to save template. Storage might be full.');
        return false;
    }
}

// 删除模板
function deleteTemplate(templateId) {
    const deleteModal = document.getElementById('deleteModal');
    const confirmBtn = document.getElementById('confirmDeleteBtn');

    confirmBtn.onclick = function() {
        try {
            let customTemplates = JSON.parse(localStorage.getItem('customTemplates')) || [];
            customTemplates = customTemplates.filter(t => t.id !== templateId);
            localStorage.setItem('customTemplates', JSON.stringify(customTemplates));
            closeDeleteModal();
            updateCustomCount();

            const container = document.getElementById('customTemplateList');
            if (container) {
                container.innerHTML = '';
                loadTemplatesForSection('custom', container);
            }

            showNotification('Template deleted successfully!');
        } catch (e) {
            console.error('Failed to delete template:', e);
            alert('Failed to delete template.');
        }
    };

    deleteModal.classList.remove('hidden');
}

// 关闭删除确认模态框
function closeDeleteModal() {
    const deleteModal = document.getElementById('deleteModal');
    deleteModal.classList.add('hidden');
    const confirmBtn = document.getElementById('confirmDeleteBtn');
    confirmBtn.onclick = null;
}

// 显示自定义模板模态框
function showCustomTemplateModal(templateId = null) {
    const modal = document.getElementById('templateModal');
    const modalTitle = document.getElementById('modalTitle');
    const templateIdInput = document.getElementById('templateId');
    const titleInput = document.getElementById('templateTitle');
    const descriptionInput = document.getElementById('templateDescription');
    const contentInput = document.getElementById('templateContent');

    if (templateId) {
        const customTemplates = JSON.parse(localStorage.getItem('customTemplates')) || [];
        const template = customTemplates.find(t => t.id === templateId);
        if (template) {
            modalTitle.textContent = 'Edit Template';
            templateIdInput.value = template.id;
            titleInput.value = template.title;
            descriptionInput.value = template.description || '';
            contentInput.value = template.content;
        }
    } else {
        modalTitle.textContent = 'Create New Template';
        templateIdInput.value = '';
        titleInput.value = '';
        descriptionInput.value = '';
        contentInput.value = '';
    }

    modal.classList.remove('hidden');
}

// 关闭模态框
function closeModal() {
    const modal = document.getElementById('templateModal');
    modal.classList.add('hidden');
}

// 保存模板
function saveTemplate(event) {
    event.preventDefault();

    const templateIdInput = document.getElementById('templateId');
    const titleInput = document.getElementById('templateTitle');
    const descriptionInput = document.getElementById('templateDescription');
    const contentInput = document.getElementById('templateContent');

    const title = titleInput.value.trim();
    const description = descriptionInput.value.trim();
    const content = contentInput.value.trim();

    if (!title || !content) {
        alert('Title and Content are required!');
        return;
    }

    const template = {
        id: templateIdInput.value,
        title: title,
        description: description,
        content: content,
        createdAt: new Date().toISOString()
    };

    const saved = saveTemplateToStorage(template);
    if (saved) {
        closeModal();
        updateCustomCount();

        const container = document.getElementById('customTemplateList');
        if (container) {
            container.innerHTML = '';
            loadTemplatesForSection('custom', container);
        }

        showNotification('Template saved successfully!');
    }
}

// 显示通知
function showNotification(message) {
    const notification = document.createElement('div');
    notification.style.cssText = `
        position: fixed;
        bottom: 20px;
        right: 20px;
        background: #28a745;
        color: white;
        padding: 15px 25px;
        border-radius: 8px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.2);
        z-index: 2000;
        animation: slideIn 0.3s ease;
    `;
    notification.textContent = message;
    document.body.appendChild(notification);

    setTimeout(() => {
        notification.style.animation = 'slideOut 0.3s ease';
        setTimeout(() => {
            document.body.removeChild(notification);
        }, 300);
    }, 3000);
}

// 添加通知动画
const style = document.createElement('style');
style.textContent = `
    @keyframes slideIn {
        from { transform: translateX(100%); opacity: 0; }
        to { transform: translateX(0); opacity: 1; }
    }
    @keyframes slideOut {
        from { transform: translateX(0); opacity: 1; }
        to { transform: translateX(100%); opacity: 0; }
    }
`;
document.head.appendChild(style);

// 页面加载完成后执行
document.addEventListener('DOMContentLoaded', function() {
    console.log('🎯 Prompt Template Library Loaded');
    loadTemplates();
    setupNavigation();
    setupModalEvents();
    hideCustomEmptyState();
});
