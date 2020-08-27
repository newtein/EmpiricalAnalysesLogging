import sys,os

# ( "Usage: run_mallet.sh input-dir output-dir")

for website in ["ALL"]:
    input_dir="Stack/"+website
    output_dir="SResults/"+website

    print(input_dir)
    print(output_dir)

    os.system("bin\mallet import-dir --input "+input_dir+" --output " +output_dir+"/source_code.sequences --keep-sequence --remove-stopwords")
        #--remove-stopwords
    print("ok")
    #mallet import-dir --input ./methods_repo/hadoop_release-2.5.0/nolog_methods_preprocessed/ --output source_code.vectors --remove-stopwords

    #exit

    os.system("bin\mallet train-topics \
        --input "+output_dir+"/source_code.sequences \
        --num-topics 500 \
        --alpha 50.0 \
        --beta 0.01 \
        --num-iterations 10000 \
        --optimize-burn-in 1000 \
        --optimize-interval 100 \
        --num-threads 4 \
        --random-seed 1 \
        --show-topics-interval 500 \
        --output-model "+output_dir+"/topic.model \
        --output-state "+output_dir+"/topic-state.gz \
        --output-topic-keys "+output_dir+"/topic_keys.dat \
        --output-doc-topics "+output_dir+"/doc_topics.dat \
        --topic-word-weights-file "+output_dir+"/topic_word_weights_file.dat \
        --diagnostics-file "+output_dir+"/diagnostics.xml \
        --word-topic-counts-file "+output_dir+"/word_topic_counts.dat \
        --xml-topic-phrase-report "+output_dir+"/topic_phrase_report.xml \
        --inferencer-filename "+output_dir+"/inferencer.mallet \
        --evaluator-filename "+output_dir+"/evaluator.mallet") #\
        #--output-topic-docs $output_dir/topic_docs.dat \
        #--num-top-docs 20 \
