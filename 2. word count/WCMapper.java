import java.io.IOException;
import org.apache.hadoop.io.*;
import org.apache.hadoop.mapred.*;

public class WCMapper extends MapReduceBase
implements Mapper<LongWritable, Text, Text, IntWritable> {

    public void map(LongWritable key, Text value,
                    OutputCollector<Text, IntWritable> output,
                    Reporter rep) throws IOException {

        String line = value.toString();

        for(String word : line.split(" ")) {
            if(word.length() > 0) {
                output.collect(new Text(word),
                               new IntWritable(1));
            }
        }
    }
}