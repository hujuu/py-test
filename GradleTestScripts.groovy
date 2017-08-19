package sample
import org.junit.Test
import geb.junit4.GebTest
import geb.Browser
import org.openqa.selenium.Keys
import org.openqa.selenium.support.ui.ExpectedCondition
import org.openqa.selenium.support.ui.WebDriverWait
import geb.driver.CachingDriverFactory

class GebSampleTest extends GebTest {
	@Test
	void search() {
		go 'https://www.google.co.jp/'
	  
		assert title == 'Google'
		
		$(name: "q").value("ラーメン")
		$(name: "btnK").click()	  
	}
}