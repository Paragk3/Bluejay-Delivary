import org.apache.poi.ss.usermodel.*;
import org.apache.poi.xssf.usermodel.XSSFWorkbook;

import java.io.FileInputStream;
import java.io.IOException;

public class Employee{
    public static void main(String args[]){
        String filepath= "Assignment_Timecard.xlsx";

        try(FileInputStream fis=new FileInputStream(filepath);
            Workbook Workbook= new XSSFWorkbook(fis)){

            Sheet sheet = Workbook.getSheetAt(0); // Assuming data is in the first sheet

            for(Row row:sheet){
                String name=row.getCell(0).getStringCellValue();
                String position = row.getCell(1).getStringCellValue();
                String daysWorked=row.getCell(2).getStringCellValue();
                int timeBetweenSwifts=(int)row.getCell(3).getStringCellValue();
                int totalHoursWorked=(int)row.getCell(4).getStringCellValue();

                if(checkConsecutiveDays(daysWorked)){
                    
                }
                )


            }

        }

    }

}
