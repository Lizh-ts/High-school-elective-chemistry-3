# 高中選修志化學3 2-6酸鹼滴定與滴定曲線 (請無視"志"字的存在)
Generate acid-base titration graphs

## 動機
在化學課時老師上到酸鹼滴定，老師問我是否能寫出一個程式，計算酸鹼滴定的pH值並繪圖，像簡報上呈現的pH滴定圖。我對此感興趣，因此決定寫一個能處理這項詢問的專案。

## 過程
我用大約2個小時構思並編程，並參考講義上的公式，使用Python並上網查如何用Python的模組作圖。然後寫到一半就發現有問題，在酸滴定鹼時會有圖形跑掉或根本不符，在和老師從原理推倒並check講義後，發現是講義的平衡常數標錯--Kb標成Ka，在修正後就正常運行了，也讓我更為了解該課程的內容。

## 心得
經過這次我發現，原來講義也會犯這種錯誤，可能是沒有給教育部審查，難怪數學老師會建議我們複習時要看課本內容(雖然他很嫌棄108課綱的編排)。這個程式我也分享給化學老師，讓之後的實驗結果若要對齊或比較時可以使用這個程式的結果；同時我也發現Python在科學計算的方便之處--不用強制定義型別，和強大的數值計算庫，使我在短時間內就處理好這個專案。過程中因為與老師討論以及理論推倒，使我對該章節的平衡算法與莫爾濃度更為熟悉，也理解滴定各時期公式的意義，同時也救回我的化學期末考。

## 使用方法
 - 壹)選擇酸鹼等級

 - 貳)選擇酸鹼滴定順序

 - 參)輸入滴定物的平衡常數(Kc)

 - 肆)輸入滴定物的體積莫耳濃度(C大M)

 - 伍)輸入被滴定物的體積莫耳濃度(C大M)

然後步驟參在強對強時不需輸入也不會顯示

我就是故意讓使用者輸入介面是cmd，絕對不是我不會做GUI

順帶一提：物理比化學簡單，希望化學分數能到80分(壓線，成就達成)

考完會有兩種"ㄨㄢˊ "，一個是"玩"樂，另一個可想而知一定是"完"蛋。

## 執行結果長這樣

<p align="left">
  <img src="P_20241118_130531.jpg" width="100%"/>
</p>
<br>
<br>
<br>
<br>
<br>

# 關於期末考的部分

考卷土石流，這很少見，通常是因為期末將至且考"完了"，書的存在並不是這麼的重要，因此開始瘋狂拋棄它們；堆積如山的考卷因磨擦力不足(微觀是電磁力)從回收桶墜落，掉到地板形成垃圾堆，因為一攤紙在那，加上破窗效應(同學的補刀)而形成考卷山丘，最後用了2小時和數次的搬運才清除。其中紙堆裡的數學課本被拿去"封印"一週沒倒的廚餘桶(這很常見但只在我們班)，不然裡面的各種微生物導致鍵結斷裂，進而各種有機物揮發，整個班上的味道會很豐富。

<p align="left">
  <img src="IMG20240628071829.jpg" width="100%"/>
</p>
