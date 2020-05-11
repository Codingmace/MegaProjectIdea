
import java.io.File;
import java.io.FilenameFilter;
import java.util.ArrayList;
import java.util.Hashtable;
import java.util.Scanner;

/**
 *
 * @author MasterWard
 */
public class Main1 {

    public static void main(String[] args) {
        File f = new File("./words");
        ArrayList<String> ar = new ArrayList();
        FilenameFilter filter = (File f1, String name) -> name.endsWith(".txt");
        File pathnames[] = f.listFiles(filter);
        Hashtable<String, Integer> dictionary = new Hashtable<>();
        for (File a : pathnames) {
            try {
                // Puts to read only to speed up maybe???
                //a.setReadOnly();
                // System.out.println(a.getPath() + " is set to readOnly");
                Scanner scan = new Scanner(a);
                while (scan.hasNextLine()) {
                    String curName = scan.nextLine().trim();
//                    System.out.println(curName);
                    Integer b = dictionary.get(curName);
                    if (b == null) { // Needs to be put in
                        dictionary.put(curName, 1);
                    } else { // It contains the value
                        dictionary.put(curName, b + 1);
                    }
//                    dictionary.get(scan.nextLine().trim());
                }
                System.out.println("The table size is: " + dictionary.size());
                System.out.println(a.getName() + " has been read");
                scan.close();
            } catch (Exception e) {
                System.out.println(a.getName() + " is a troubling file");
                System.out.println(e.getMessage());
                return;
            } finally {
                System.out.println();
            }
        }

    }

}
