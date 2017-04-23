package galactus.ron.trigcalc24;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;


import android.view.View; import android.widget.Button; import android.widget.EditText;
import android.widget.TextView;
import android.widget.Toast;

import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.InputStreamReader;

public class MainActivity extends AppCompatActivity implements View.OnClickListener
{
    private Button btnsin,btncos,btntan,btnadd,btnsub,btnmul,btndiv,btnSqrt,btnSav,btnRec,btnClr;
    private EditText etnum,etres,etnum2;
    private TextView operator;
    private static double memoryValue,inputvalue;
    String filename="SciMemValue.txt";
    String message;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState); setContentView(R.layout.activity_main);
        init();
    }
    private void init(){
        operator= (TextView) findViewById(R.id.operator);
        operator.setVisibility(View.GONE);
        btnsin=(Button)findViewById(R.id.btnSin);
        btncos=(Button)findViewById(R.id.btnCos);
        btntan=(Button)findViewById(R.id.btnTan);
        btnadd=(Button)findViewById(R.id.btnAdd);
        btnsub=(Button)findViewById(R.id.btnSub);
        btnmul=(Button)findViewById(R.id.btnMult);
        btndiv=(Button)findViewById(R.id.btnDiv);
        btnSqrt=(Button)findViewById(R.id.btnsqrt);
        btnClr=(Button)findViewById(R.id.btnclr);
        btnRec=(Button)findViewById(R.id.btnmr);
        btnSav=(Button)findViewById(R.id.btnms);
        etnum=(EditText)findViewById(R.id.etNum);
        etnum2=(EditText)findViewById(R.id.etNum2);
        etres=(EditText)findViewById(R.id.tvResult);
        btnsin.setOnClickListener(this);
        btncos.setOnClickListener(this);
        btntan.setOnClickListener(this);
        btnadd.setOnClickListener(this);
        btnsub.setOnClickListener(this);
        btnmul.setOnClickListener(this);
        btndiv.setOnClickListener(this);
        btnSqrt.setOnClickListener(this);
        btnClr.setOnClickListener(this);
        btnRec.setOnClickListener(this);
        btnSav.setOnClickListener(this);
    }
    public void onClick(View view){
        String num1=etnum.getText().toString();

        switch(view.getId()){
            case R.id.btnSin:
                double sin=Math.sin(Math.toRadians(Double.parseDouble(num1)));//output in Radian
                //convert radian into degrees
                //  sin = (sin * 3.14)/ 180;
                etres.setText(String.valueOf(sin));
                break;
            case R.id.btnCos:
                double Cos=Math.cos(Math.toRadians(Double.parseDouble(num1)));
                etres.setText(String.valueOf(Cos));
                break;
            case R.id.btnTan:
                double Tan=Math.tan(Math.toRadians(Double.parseDouble(num1)));
                etres.setText(String.valueOf(Tan));
                break;
            case R.id.btnSub:

                operator.setText("-");
                operator.setVisibility(View.VISIBLE);
                double sub=Double.parseDouble(etnum2.getText().toString())- Double.parseDouble(num1);
                etres.setText(String.valueOf(sub));
                break;
            case R.id.btnAdd:
                operator.setText("+");
                operator.setVisibility(View.VISIBLE);
                double add=Double.parseDouble(etnum2.getText().toString())+Double.parseDouble(num1);
                etres.setText(String.valueOf(add));
                break;
            case R.id.btnMult:

                operator.setText("*");
                operator.setVisibility(View.VISIBLE);
                double mul=Double.parseDouble(etnum2.getText().toString())*Double.parseDouble(num1);
                etres.setText(String.valueOf(mul));
                break;
            case R.id.btnDiv:

                operator.setText("/");
                operator.setVisibility(View.VISIBLE);
                double div=Double.parseDouble(etnum2.getText().toString())/Double.parseDouble(num1);
                etres.setText(String.valueOf(div));
                break;
            case R.id.btnsqrt:
                double sqrt=Math.sqrt(Double.parseDouble(num1));
                etres.setText(String.valueOf(sqrt));
                break;
            case R.id.btnclr:
                memoryValue = Double.NaN;
                etres.setText("0");
                inputvalue= Double.parseDouble(etres.getText().toString());
                    memoryValue = inputvalue;
                    etres.setText(String.valueOf(memoryValue));
                    String value= etres.getText().toString();

                    try {
                        FileOutputStream fileOutputStream=openFileOutput(filename,MODE_PRIVATE);
                        fileOutputStream.write(value.getBytes());
                        fileOutputStream.close();
                        Toast.makeText(getApplicationContext(),"saved to text file",Toast.LENGTH_LONG).show();
                    } catch (FileNotFoundException e) {
                        e.printStackTrace();
                    } catch (IOException e) {
                        e.printStackTrace();
                    }
                break;
            case R.id.btnmr:
                if (Double.isNaN(memoryValue)) {
                    etres.setText("no data");
                }
                else

                try {
                    FileInputStream fileInputStream= openFileInput(filename);
                    InputStreamReader inputStreamReader= new InputStreamReader(fileInputStream);
                    BufferedReader bufferedReader=new BufferedReader(inputStreamReader);
                    StringBuffer stringBuffer= new StringBuffer();
                    while((message=bufferedReader.readLine())!=null)
                    {
                        stringBuffer.append(message);
                    }
                    etres.setText(stringBuffer.toString());
                } catch (FileNotFoundException e) {
                    e.printStackTrace();
                } catch (IOException e) {
                    e.printStackTrace();
                }
                   // etres.setText(String.valueOf((int)memoryValue));
                break;
            case R.id.btnms:
                inputvalue= Double.parseDouble(etres.getText().toString());
                if (Double.isNaN(inputvalue)){
                    etres.setText("no data");
                }
                else {
                    memoryValue = inputvalue;
                    etres.setText(String.valueOf(memoryValue));
                    value = etres.getText().toString();

                    try {
                        FileOutputStream fileOutputStream=openFileOutput(filename,MODE_PRIVATE);
                        fileOutputStream.write(value.getBytes());
                        fileOutputStream.close();
                        Toast.makeText(getApplicationContext(),"saved to text file",Toast.LENGTH_LONG).show();
                    } catch (FileNotFoundException e) {
                        e.printStackTrace();
                    } catch (IOException e) {
                        e.printStackTrace();
                    }
                }
                break;
        }
    }
    public void saveValue(View view){

        String value= etres.getText().toString();

        try {
            FileOutputStream fileOutputStream=openFileOutput(filename,MODE_PRIVATE);
            fileOutputStream.write(value.getBytes());
            fileOutputStream.close();
            Toast.makeText(getApplicationContext(),"saved to text file",Toast.LENGTH_LONG).show();
        } catch (FileNotFoundException e) {
            e.printStackTrace();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
    public void loadValue(View view){
        String message;
        try {
            FileInputStream fileInputStream= openFileInput(filename);
            InputStreamReader inputStreamReader= new InputStreamReader(fileInputStream);
            BufferedReader bufferedReader=new BufferedReader(inputStreamReader);
            StringBuffer stringBuffer= new StringBuffer();
            while((message=bufferedReader.readLine())!=null)
            {
                stringBuffer.append(message);
            }
            etres.setText(stringBuffer.toString());
        } catch (FileNotFoundException e) {
            e.printStackTrace();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}