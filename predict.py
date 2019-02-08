import tensorflow as tf, sys


def classifySkinLesion(image_path):
   
    image_data = tf.gfile.FastGFile(image_path, 'rb').read()


    label_lines = [line.rstrip() for line 
                       in tf.gfile.GFile("HackathonProject/ISIC_3/retrained_labels.txt")]

    with tf.gfile.FastGFile("HackathonProject/ISIC_3/retrained_graph.pb", 'rb') as f:
        graph_def = tf.GraphDef()
        graph_def.ParseFromString(f.read())
        _ = tf.import_graph_def(graph_def, name='')

    with tf.Session() as sess:
    
        softmax_tensor = sess.graph.get_tensor_by_name('final_result:0')
        
        predictions = sess.run(softmax_tensor, \
                 {'DecodeJpeg/contents:0': image_data})
        
        top_k = predictions[0].argsort()[-len(predictions[0]):][::-1]
        
        for node_id1 in top_k:
            if(node_id1==0):
                human_string1 = label_lines[node_id1]
                score1 = predictions[0][node_id1]
            else: 
                human_string2 = label_lines[node_id1]
                score2 = predictions[0][node_id1]    
        if(score1>score2):
            dic={
                     human_string1:`score1`
                }
            return dic
            # return('%s (score = %.5f)' % (human_string1, score1))
        else:
            dic={
                     human_string2:`score2`
                }
            return dic
            # return('%s (score = %.5f)' % (human_string2, score2))    
            # print('%s (score = %.5f)' % (human_string, score))
    # return('%s (score = %.5f)' % (human_string, score))
     #   dic={
     #       human_string:`score`
    #    }
   # return dic


def classifyDiabeticRetinopathy(image_path):
   
    image_data = tf.gfile.FastGFile(image_path, 'rb').read()

    # Loads label file, strips off carriage return
  #  label_lines = [line.rstrip() for line 
   #                    in tf.gfile.GFile("HackathonProject/retino/retrained_labels.txt")]

    # Unpersists graph from file
    with tf.gfile.FastGFile("HackathonProject/retino/retrained_graph.pb", 'rb') as f:
        graph_def = tf.GraphDef()
        graph_def.ParseFromString(f.read())
        _ = tf.import_graph_def(graph_def, name='')

    with tf.Session() as sess:
        # Feed the image_data as input to the graph and get first prediction
        softmax_tensor = sess.graph.get_tensor_by_name('final_result:0')
        
        predictions = sess.run(softmax_tensor, \
                 {'DecodeJpeg/contents:0': image_data})
        
        # Sort to show labels of first prediction in order of confidence
        top_k = predictions[0].argsort()[-len(predictions[0]):][::-1]
        
        for node_id in top_k:
            if (node_id==0):
               #human_string = label_lines[node_id]
               human_string1="No symptoms found."
               score1 = predictions[0][node_id]
            #    print('%s (score = %.5f)' % (human_string1, score1))
            elif (node_id==1):
                human_string2="Mild case"
                score2 = predictions[0][node_id]
                # print('%s (score = %.5f)' % (human_string2, score2))
            else:
                human_string3="Severe case"
                score3 = predictions[0][node_id]
                # print('%s (score = %.5f)' % (human_string3, score3))
        if(score1>score2):
            if(score1>score3):
                dic={
                    human_string1:`score1`
                    }
                return dic

        if(score2>score1):
            if(score2>score3):
                dic={
                    human_string2:`score2`
                    }
                return dic
        else:
            dic={
                    human_string3:`score3`
                }
            return dic
    # return('%s (score = %.5f)' % (human_string1, score1),(human_string2, score2),(human_string3, score3))
    
   # return('%s (score = %.5f)' % (human_string2, score2))
   # return('%s (score = %.5f)' % (human_string3, score3))